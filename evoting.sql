-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: evoting
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.22.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `candidates`
--

DROP TABLE IF EXISTS `candidates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `candidates` (
  `voter_id` int NOT NULL,
  `post_id` varchar(50) DEFAULT NULL,
  `votes` int DEFAULT NULL,
  PRIMARY KEY (`voter_id`),
  KEY `post_id` (`post_id`),
  CONSTRAINT `candidates_ibfk_1` FOREIGN KEY (`voter_id`) REFERENCES `voters` (`id`) ON DELETE CASCADE,
  CONSTRAINT `candidates_ibfk_2` FOREIGN KEY (`post_id`) REFERENCES `positions` (`post`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `candidates`
--

LOCK TABLES `candidates` WRITE;
/*!40000 ALTER TABLE `candidates` DISABLE KEYS */;
INSERT INTO `candidates` VALUES (2,'President',1),(3,'Sports',1),(4,'President',0),(6,'Sports',0);
/*!40000 ALTER TABLE `candidates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `positions`
--

DROP TABLE IF EXISTS `positions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `positions` (
  `post` varchar(50) NOT NULL,
  PRIMARY KEY (`post`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `positions`
--

LOCK TABLES `positions` WRITE;
/*!40000 ALTER TABLE `positions` DISABLE KEYS */;
INSERT INTO `positions` VALUES ('President'),('Sports');
/*!40000 ALTER TABLE `positions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `voters`
--

DROP TABLE IF EXISTS `voters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `voters` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `auth_id` varchar(50) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `voters`
--

LOCK TABLES `voters` WRITE;
/*!40000 ALTER TABLE `voters` DISABLE KEYS */;
INSERT INTO `voters` VALUES (1,'ADMIN','admin.com','admin',''),(2,'voter2','voter2@student.com','admin','SportsPresident'),(3,'voter3','voter3@student.com','admin',''),(4,'voter4','voter4@student.com','admin',''),(5,'voter5','voter5@student.com','admin',''),(6,'voter6','voter6@student.com','admin',''),(7,'voter7','voter7@student.com','admin',''),(8,'voter8','voter8@student.com','admin',''),(9,'voter9','voter9@student.com','admin',''),(10,'voter10','voter10@student.com','admin',''),(11,'voter11','voter11@student.com','admin',''),(12,'voter12','voter12@student.com','admin',''),(13,'voter13','voter13@student.com','admin',''),(14,'voter14','voter14@student.com','admin',''),(15,'voter15','voter15@student.com','admin',''),(16,'voter16','voter16@student.com','admin',''),(17,'voter17','voter17@student.com','admin',''),(18,'voter18','voter18@student.com','admin',''),(19,'voter19','voter19@student.com','admin',''),(20,'voter20','voter20@student.com','admin',''),(21,'voter21','voter21@student.com','admin',''),(22,'voter22','voter22@student.com','admin',''),(23,'voter23','voter23@student.com','admin',''),(24,'voter24','voter24@student.com','admin',''),(25,'voter25','voter25@student.com','admin',''),(26,'voter26','voter26@student.com','admin',''),(27,'voter27','voter27@student.com','admin',''),(28,'voter28','voter28@student.com','admin',''),(29,'voter29','voter29@student.com','admin',''),(30,'voter30','voter30@student.com','admin',''),(31,'voter31','voter31@student.com','admin',''),(32,'voter32','voter32@student.com','admin',''),(33,'voter33','voter33@student.com','admin',''),(34,'voter34','voter34@student.com','admin',''),(35,'voter35','voter35@student.com','admin',''),(36,'voter36','voter36@student.com','admin',''),(37,'voter37','voter37@student.com','admin',''),(38,'voter38','voter38@student.com','admin',''),(39,'voter39','voter39@student.com','admin',''),(40,'voter40','voter40@student.com','admin',''),(41,'voter41','voter41@student.com','admin',''),(42,'voter42','voter42@student.com','admin',''),(43,'voter43','voter43@student.com','admin',''),(44,'voter44','voter44@student.com','admin',''),(45,'voter45','voter45@student.com','admin',''),(46,'voter46','voter46@student.com','admin',''),(47,'voter47','voter47@student.com','admin',''),(48,'voter48','voter48@student.com','admin',''),(49,'voter49','voter49@student.com','admin',''),(50,'voter50','voter50@student.com','admin','');
/*!40000 ALTER TABLE `voters` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-02 16:40:31
