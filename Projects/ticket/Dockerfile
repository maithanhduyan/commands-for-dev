# Giai đoạn 1: Sử dụng Maven image để build dự án
FROM maven:3.9.9-ibm-semeru-21-jammy AS builder

# Đặt thư mục làm việc trong container
WORKDIR /app

# Copy file pom.xml và các file cấu hình Maven
COPY pom.xml ./
COPY src ./src

# Build ứng dụng
RUN mvn clean package -DskipTests

# Giai đoạn 2: sử dụng OpenJDK để chạy ứng dụng
FROM openjdk:21

# Tạo một thư mục cho ứng dụng
VOLUME /tmp

# Copy file JAR từ giai đoạn build trước vào container
COPY --from=builder /app/target/*.jar app.jar

# Chạy ứng dụng Spring Boot
ENTRYPOINT ["java", "-jar", "/app.jar"]

# Expose port 8080
EXPOSE 8080