FROM python:3.10.0


SHELL ["/bin/bash", "-c"]

# set env vars

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

RUN pip install --upgrade pip

# quite and yes always  libjpeg-dev:
RUN apt update && apt -qy install \
    # GNU Compiler Collection
    gcc \
    # This package depends on default Debian implementation of libjpeg.so.62 JPEG library.
    libjpeg-dev \
    # XML stylesheet transformation library (development files)
    libxslt-dev \
    gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash player && chmod 777 /opt /run

# create dir and cd
WORKDIR /player

RUN mkdir /player/static && mkdir /player/media && chown -R player:player /player && chmod 755 /player

COPY --chown=player:player . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8001", "media_player.wsgi:application"]