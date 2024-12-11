FROM python:3.13.1-slim-bookworm

ENV JAVA_HOME=/opt/java/openjdk

COPY --from=eclipse-temurin:17-jre $JAVA_HOME $JAVA_HOME

ENV PATH="${JAVA_HOME}/bin:${PATH}"

RUN apt update && \
    apt install --no-install-recommends --no-install-suggests chromium wget -y && \
    wget https://github.com/allure-framework/allure2/releases/download/2.32.0/allure-2.32.0.tgz && \
    tar xf allure-2.32.0.tgz -C /opt && \
    rm allure-2.32.0.tgz

RUN ln -s /opt/allure-2.32.0/bin/allure /usr/bin/allure

WORKDIR /framework

COPY ./requirements.txt /framework

RUN pip install --no-cache-dir -r requirements.txt
