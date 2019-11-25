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
    cd /plc && ./waf configure && ./waf install

# Download data files
RUN curl "http://pla.esac.esa.int/pla/aio/product-action?COSMOLOGY.FILE_ID=COM_Likelihood_Data-baseline_R3.00.tar.gz" -o data.tar.gz && \
    tar zxvfs data.tar.gz && \
    mkdir /data && mv baseline/plc_3.0 /data/clik_14.0

# Set up working directory
RUN mkdir /app
WORKDIR /app
ADD . /app

# Symlink in the data
RUN ln -s /data/clik_14.0 /app/data/clik_14.0

# Finally make CosmoMC
RUN cd /app && bash -c "source /plc/bin/clik_profile.sh && make clean && make"
RUN echo "\n\nsource /plc/bin/clik_profile.sh" >> ~/.bashrc
CMD ["/bin/bash"]
