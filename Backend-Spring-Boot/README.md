# Real-Time Ad Analytics Backend

This is the backend system for a real-time advertisement analytics platform. It is built using **Java Spring Boot** and designed to track advertisement **impressions and clicks**, store **user interaction metadata**, and serve **aggregated analytics** to the frontend.

## Overview

The backend exposes several REST API endpoints for logging ad interactions and retrieving real-time analytics. It integrates with a **PostgreSQL** database and uses the **GeoIP2** library to enrich click data with geographic location.

## Features

- Track banner and video ad **clicks** and **impressions**
- Save interaction metadata: `adId`, `deviceType`, `browser`, `timestamp`, `type`
- Enrich clicks with `city`, `state`, and `country` using GeoIP2
- REST endpoints for:
  - Logging analytics
  - Recording click events
  - Viewing aggregated ad performance (CTR, impressions, clicks)
  - Viewing detailed click logs

## Folder Structure

`com.realtimecausation.masters` is the base package. It contains the following sub-packages:

- **controller/** – REST API endpoints for frontend communication  
  - `AdAnalyticsEventController.java`: Handles impressions and clicks storage  
  - `AdClickController.java`: Logs click metadata using GeoIP  
  - `ClickEventController.java`: Returns all raw click events for admin view  

- **dto/** – Request/Response payload classes for handling frontend communication  
  - `AdAnalyticsRequest.java` / `AdAnalyticsResponse.java`  
  - `AdResponse.java`  
  - `ClickRequest.java`  

- **model/** – JPA entity classes representing database tables  
  - `AdAnalyticsEvent.java`  
  - `AdClickEvent.java`  
  - `ClickEvent.java`  

- **repository/** – JPA repositories for accessing database  
  - `AdAnalyticsEventRepository.java`  
  - `AdClickEventRepository.java`  
  - `ClickEventRepository.java`  

- **MastersApplication.java** – Main class with Spring Boot entry point  

## API Endpoints

1. `POST /api/log`  
   Records or updates ad impressions and clicks (aggregated).  
   Request Body: `AdAnalyticsRequest`  
   Fields: `adId`, `impressions`, `clicks`

2. `GET /api/analytics`  
   Returns all ad analytics with calculated CTR (Click Through Rate)  
   Response: List of `AdAnalyticsResponse`

3. `POST /api/ads/click`  
   Logs a single click event with metadata and location info using GeoIP2  
   Request Body: `AdResponse`  
   Fields: `adId`, `type`, `deviceType`, `browser`

4. `GET /api/clicks`  
   Returns raw click log data for admin viewing  
   Response: List of `ClickEvent`

## Database Configuration

This project uses PostgreSQL. The configuration is defined in `application.properties`:

```
spring.application.name=masters
spring.datasource.url=jdbc:postgresql://localhost:5432/movieanalytics
spring.datasource.username=postgres
spring.datasource.password=YOUR_PASSWORD
server.port=8081
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect
```

Two main tables are created automatically:

- `ad_analytics_events` – Stores total impressions and clicks per ad
- `ad_click_events` – Stores each click with timestamp, IP-derived location, and browser info

## GeoIP2 Integration

We use the `GeoLite2-City.mmdb` file with MaxMind’s GeoIP2 Java library to determine the user's:

- City  
- State  
- Country  

This information is added to each ad click record in `AdClickEvent`.

In local testing, if the IP is localhost (`127.0.0.1` or `::1`), it defaults to a public IP like `8.8.8.8` for simulation.

## Technologies Used

- Java 21  
- Spring Boot 3.4.4  
- Spring Data JPA  
- PostgreSQL  
- GeoIP2 (MaxMind)  
- Hibernate  

## Usage

1. Make sure PostgreSQL is running and database `movieanalytics` exists  
2. Build and run the project using:

   ```
   mvn clean install
   mvn spring-boot:run
   ```

3. Backend will run at `http://localhost:8081`  
4. Use tools like Postman or a React frontend to make requests

## Postman Testing

Postman is used for testing `POST /api/log` and `POST /api/ads/click` endpoints.

We created **bulk test cases** with various ad IDs and types (video/banner) to simulate real interaction data and test GeoIP logging.
