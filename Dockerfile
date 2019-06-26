FROM kbase/sdkbase2:python
MAINTAINER KBase Developer
# -----------------------------------------

# RUN apt-get update


# -----------------------------------------

RUN pip install --upgrade pip
RUN pip install cobra
RUN pip install escher
RUN pip install networkx
RUN pip install cobrakbase==0.1.9

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod -R a+rw /kb/module

WORKDIR /kb/module

RUN make all

RUN mkdir -p /root/.cache
RUN tar -xf /kb/module/data/escher.tar.gz -C /root/.cache

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
