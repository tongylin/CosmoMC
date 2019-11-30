FROM cmbant/cosmobox:latest
LABEL MAINTAINER="Ben Hughes <me@benhughes.name"

# Install Ubuntu packages
RUN apt-get update && apt-get install -y \
    curl \
    liblapack3 \
    liblapack-dev \
    libopenblas-base \
    libopenblas-dev \
    liblapacke-dev

# Manually install cfitsio
RUN wget http://heasarc.gsfc.nasa.gov/FTP/software/fitsio/c/cfitsio-3.47.tar.gz && \
    tar zxvf cfitsio-3.47.tar.gz && \
    cd cfitsio-3.47/ && \
    ./configure --prefix=/usr && \
    make && \
    make install && \
    make clean

# Download and compile plc
RUN curl "http://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_Likelihood_Code-v3.0_R3.01.tar.gz" -o plc.tar.gz && \
    tar zxvfs plc.tar.gz && \
    mv code/plc_3.0/plc-3.01 /plc && \
    rm plc.tar.gz && rm -rf code && \
    cd /plc && ./waf configure && ./waf install && \
    echo "\n\nsource /plc/bin/clik_profile.sh" >> ~/.bash_profile && \
    echo "\n\nsource /plc/bin/clik_profile.sh" >> ~/.bashrc

# Set up working directory (will require mounting via "docker run" as "-v $(pwd):/app")
VOLUME ["/app"]
WORKDIR /app
COPY docker-entrypoint.sh /usr/local/bin

# Run bash by default, but use docker-entrypoint.sh to allow for other commands to be wrapped
# in plc-required clik_profile.sh modifications:
#
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["/bin/bash"]