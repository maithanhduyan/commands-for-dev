FROM golang:1.22.5-bullseye
RUN mkdir /app
ADD ./main.go /app/
WORKDIR /app
RUN go mod init app
RUN go mod tidy
RUN go build main.go 
EXPOSE 8080
# RUN go build -o main ./...
CMD ["/app/main"]