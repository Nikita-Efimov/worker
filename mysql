-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: worker
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `worker`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `worker` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `worker`;

--
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text,
  `desciption` text,
  `category` text,
  `const` int(11) DEFAULT NULL,
  `deadline` text,
  `owner` text,
  `requests` text,
  `parent` int(11) DEFAULT NULL,
  `child` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task`
--

LOCK TABLES `task` WRITE;
/*!40000 ALTER TABLE `task` DISABLE KEYS */;
INSERT INTO `task` VALUES (3,'Test','Test','Test',0,'2018-12-11','admin',NULL,NULL,NULL),(4,'Test Task','Task for test','Testting',5000,'2018-12-12','admin',NULL,NULL,NULL),(5,'123','123','123',123,'2018-12-04','admin',NULL,NULL,NULL),(6,'1','1','1',1,'2018-12-11','admin',NULL,NULL,NULL),(7,'Разработка веб ресурса','Необходимо сделать ресурс по заданию хакатона, срочно!!!!(текущий проект)','Web,Hackaton',5000,'2018-12-09','admin',NULL,NULL,'3,6,8,9,10'),(8,'New','Test','123',5000,'2018-12-09','admin',NULL,7,'15'),(9,'New1','Testim','123',5000,'2018-12-09','admin',NULL,7,NULL),(10,'Go','Testit','123',5000,'2018-12-09','admin',NULL,7,'14,17'),(11,'Go1','123','123',5000,'2018-12-09','admin',NULL,10,NULL),(12,'Go1','123','123',5000,'2018-12-09','admin',NULL,10,NULL),(13,'Go2','GOGOO','123',5000,'2018-12-09','admin',NULL,10,NULL),(14,'Go3','GOOGOGOGO','123',5000,'2018-12-09','admin',NULL,10,'16'),(15,'Newr','123','123',5000,'2018-12-09','admin',NULL,8,NULL),(16,'Go4','123','123',5000,'2018-12-09','admin',NULL,14,NULL),(17,'TEGO','GOTE','123',5000,'2018-12-09','admin',NULL,10,NULL);
/*!40000 ALTER TABLE `task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `login` text,
  `password` text,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('admin@admin.admin','1234',1),('test1@test.test','1234',2);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img` text,
  `bio` text,
  `email` text,
  `phone` text,
  `finished_tasks` int(11) DEFAULT NULL,
  `abilities` text,
  `registration_date` datetime DEFAULT NULL,
  `name` text,
  `surname` text,
  `created_tasks` int(11) DEFAULT NULL,
  `taked_tasks` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
INSERT INTO `user_info` VALUES (1,NULL,'working','admin@admin.admin',NULL,100500,'прогатb',NULL,'Admin',NULL,100500,'7');
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-09 10:40:03
