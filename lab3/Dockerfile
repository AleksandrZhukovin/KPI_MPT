FROM ubuntu:latest

RUN apk update && apk upgrade && apk add bash
RUN apk --no-cache add lua5.3 lua5.3-dev luarocks5.3

COPY . .

RUN luarocks install busted && luarocks install luassert

CMD ["busted", "garbage_collector_test.lua"]
CMD ["busted", "heap_test.lua"]
CMD ["busted", "reference_types_test.lua"]
CMD ["busted", "value_types_test.lua"]