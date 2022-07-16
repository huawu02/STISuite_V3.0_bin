#
# docker build --no-cache -t stisuite -f gear/Dockerfile .
#
#
# Start with the Matlab r2018b runtime container
FROM flywheel/matlab-mcr:v95
# Install Python
RUN apt-get -qq update && apt-get -qq -y install \
    python python-pip 
# for MATLAB Signal Processing Toolbox (findpeaks)
RUN apt-get install -y libasound2 libatk1.0-0

# Copy shell script and MCR binary to /bin
COPY STI_pipeline_CNI /bin
COPY run_STI_pipeline_CNI.sh /bin
COPY dcm2niix /bin

# change permissions 
RUN chmod +x /bin/*

# Make directory for flywheel spec
ENV FLYWHEEL /flywheel/v0
RUN mkdir -p ${FLYWHEEL}

# Copy and configure run script and metadata code
COPY gear/run.py ${FLYWHEEL}/run
RUN chmod +x ${FLYWHEEL}/run
COPY gear/manifest.json ${FLYWHEEL}/manifest.json

# Configure entrypoint
ENTRYPOINT ["/flywheel/v0/run"]
