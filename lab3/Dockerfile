FROM ubuntu:latest

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y lua5.3 lua5.3-dev luarocks

COPY . .

RUN luarocks install busted && luarocks install luassert

CMD ["busted", "lab3/"]