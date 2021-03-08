FROM openjdk:11-jre-slim
COPY target/*.jar app.jar
EXPOSE 4000
ENTRYPOINT ["java","-jar","app.jar"]