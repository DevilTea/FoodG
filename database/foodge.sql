-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: foodge
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attribute`
--

DROP TABLE IF EXISTS `attribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `attribute` (
  `idATTRIBUTE` int(11) NOT NULL AUTO_INCREMENT,
  `nameATTRIBUTE` varchar(10) NOT NULL,
  `statement` int(11) NOT NULL,
  PRIMARY KEY (`idATTRIBUTE`),
  UNIQUE KEY `idATTRIBUTE_UNIQUE` (`idATTRIBUTE`),
  UNIQUE KEY `nameATTRIBUTE_UNIQUE` (`nameATTRIBUTE`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attribute`
--

LOCK TABLES `attribute` WRITE;
/*!40000 ALTER TABLE `attribute` DISABLE KEYS */;
INSERT INTO `attribute` VALUES (1,'冷食',0),(2,'熱食',0),(3,'不怎麼餓',3),(4,'很餓',3),(5,'有時間',3),(6,'趕時間',3),(7,'高價',1),(8,'平價',1),(9,'日式',1),(10,'中式',1),(11,'美式',1),(12,'獨自一人',2),(13,'一大群人',2),(14,'三兩個人',2),(15,'下午茶',0),(16,'輕食',1),(17,'高熱量',1),(18,'重口味',1),(19,'清淡',1),(20,'情侶',2),(21,'飯',0),(22,'麵',0),(23,'宵夜',0),(24,'晚餐',0),(25,'午餐',0),(26,'早餐',0),(27,'外送',1),(28,'內用',1),(29,'外帶',1),(30,'方便攜帶',1);
/*!40000 ALTER TABLE `attribute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food`
--

DROP TABLE IF EXISTS `food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `food` (
  `idFOOD` int(11) NOT NULL AUTO_INCREMENT,
  `nameFOOD` varchar(10) NOT NULL,
  PRIMARY KEY (`idFOOD`),
  UNIQUE KEY `idFOOD_UNIQUE` (`idFOOD`),
  UNIQUE KEY `nameFOOD_UNIQUE` (`nameFOOD`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food`
--

LOCK TABLES `food` WRITE;
/*!40000 ALTER TABLE `food` DISABLE KEYS */;
INSERT INTO `food` VALUES (22,'冰淇淋'),(9,'咖哩飯'),(26,'夜市'),(14,'小籠包'),(15,'御飯糰'),(16,'微波食品'),(2,'拉麵'),(29,'日式定食'),(21,'早餐店'),(10,'泡麵'),(30,'海產店'),(23,'涼麵'),(27,'滷肉飯'),(13,'火鍋'),(5,'炒飯'),(6,'炒麵'),(1,'烏龍麵'),(25,'燒烤'),(28,'牛排'),(17,'粥'),(19,'素食'),(8,'義大利麵'),(3,'自助餐'),(4,'速食店'),(24,'鐵板燒'),(12,'關東煮'),(18,'雞排'),(20,'鬆餅'),(11,'麵包'),(7,'麵線');
/*!40000 ALTER TABLE `food` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food_has_attribute`
--

DROP TABLE IF EXISTS `food_has_attribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `food_has_attribute` (
  `FOOD_idFOOD` int(11) NOT NULL,
  `ATTRIBUTE_idATTRIBUTE` int(11) NOT NULL,
  PRIMARY KEY (`FOOD_idFOOD`,`ATTRIBUTE_idATTRIBUTE`),
  KEY `fk_FOOD_has_ATTRIBUTE_ATTRIBUTE1_idx` (`ATTRIBUTE_idATTRIBUTE`),
  KEY `fk_FOOD_has_ATTRIBUTE_FOOD_idx` (`FOOD_idFOOD`),
  CONSTRAINT `fk_FOOD_has_ATTRIBUTE_ATTRIBUTE1` FOREIGN KEY (`ATTRIBUTE_idATTRIBUTE`) REFERENCES `attribute` (`idATTRIBUTE`),
  CONSTRAINT `fk_FOOD_has_ATTRIBUTE_FOOD` FOREIGN KEY (`FOOD_idFOOD`) REFERENCES `food` (`idfood`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food_has_attribute`
--

LOCK TABLES `food_has_attribute` WRITE;
/*!40000 ALTER TABLE `food_has_attribute` DISABLE KEYS */;
INSERT INTO `food_has_attribute` VALUES (1,1),(4,1),(11,1),(15,1),(21,1),(22,1),(23,1),(26,1),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2),(9,2),(10,2),(12,2),(13,2),(14,2),(16,2),(17,2),(18,2),(19,2),(21,2),(24,2),(25,2),(26,2),(27,2),(28,2),(29,2),(30,2),(3,3),(4,3),(11,3),(12,3),(14,3),(15,3),(16,3),(18,3),(19,3),(20,3),(21,3),(22,3),(23,3),(26,3),(27,3),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(8,4),(9,4),(13,4),(17,4),(19,4),(21,4),(24,4),(25,4),(27,4),(29,4),(30,4),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(13,5),(20,5),(21,5),(22,5),(23,5),(24,5),(25,5),(26,5),(27,5),(29,5),(30,5),(3,6),(4,6),(10,6),(11,6),(12,6),(14,6),(15,6),(16,6),(18,6),(21,6),(23,6),(26,6),(2,7),(4,7),(8,7),(13,7),(20,7),(22,7),(25,7),(27,7),(29,7),(30,7),(1,8),(3,8),(4,8),(5,8),(6,8),(7,8),(9,8),(10,8),(11,8),(13,8),(15,8),(16,8),(17,8),(18,8),(19,8),(21,8),(24,8),(26,8),(27,8),(30,8),(1,9),(2,9),(9,9),(12,9),(15,9),(23,9),(29,9),(3,10),(5,10),(6,10),(7,10),(14,10),(17,10),(24,10),(26,10),(27,10),(30,10),(4,11),(27,11),(1,12),(2,12),(3,12),(4,12),(5,12),(6,12),(7,12),(10,12),(11,12),(12,12),(13,12),(14,12),(15,12),(16,12),(18,12),(19,12),(21,12),(22,12),(23,12),(25,12),(26,12),(27,12),(1,13),(2,13),(4,13),(8,13),(9,13),(13,13),(19,13),(24,13),(25,13),(26,13),(27,13),(29,13),(30,13),(1,14),(2,14),(3,14),(4,14),(5,14),(6,14),(7,14),(8,14),(9,14),(13,14),(17,14),(18,14),(19,14),(20,14),(21,14),(22,14),(23,14),(24,14),(25,14),(26,14),(27,14),(29,14),(30,14),(11,15),(12,15),(20,15),(22,15),(11,16),(12,16),(15,16),(20,16),(21,16),(22,16),(23,16),(2,17),(4,17),(8,17),(9,17),(13,17),(18,17),(22,17),(24,17),(25,17),(26,17),(27,17),(30,17),(2,18),(4,18),(9,18),(10,18),(13,18),(18,18),(24,18),(25,18),(26,18),(27,18),(1,19),(12,19),(19,19),(23,19),(1,20),(2,20),(8,20),(20,20),(22,20),(26,20),(27,20),(29,20),(3,21),(5,21),(6,21),(7,21),(9,21),(17,21),(19,21),(24,21),(26,21),(27,21),(29,21),(30,21),(1,22),(2,22),(3,22),(8,22),(10,22),(19,22),(21,22),(23,22),(24,22),(26,22),(4,23),(10,23),(11,23),(12,23),(14,23),(15,23),(18,23),(23,23),(26,23),(1,24),(2,24),(3,24),(4,24),(5,24),(6,24),(7,24),(8,24),(9,24),(10,24),(11,24),(13,24),(16,24),(17,24),(19,24),(23,24),(24,24),(25,24),(26,24),(27,24),(29,24),(30,24),(1,25),(2,25),(3,25),(4,25),(5,25),(6,25),(7,25),(8,25),(9,25),(10,25),(11,25),(13,25),(16,25),(17,25),(19,25),(23,25),(24,25),(25,25),(27,25),(29,25),(30,25),(4,26),(11,26),(14,26),(15,26),(21,26),(27,26),(4,27),(1,28),(2,28),(3,28),(4,28),(5,28),(6,28),(7,28),(8,28),(9,28),(13,28),(17,28),(19,28),(20,28),(21,28),(22,28),(23,28),(24,28),(25,28),(26,28),(27,28),(29,28),(30,28),(1,29),(3,29),(4,29),(5,29),(6,29),(7,29),(14,29),(17,29),(18,29),(19,29),(21,29),(22,29),(23,29),(26,29),(27,29),(4,30),(10,30),(11,30),(12,30),(14,30),(15,30),(16,30),(18,30),(21,30),(22,30),(23,30),(26,30);
/*!40000 ALTER TABLE `food_has_attribute` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-14 10:24:11
