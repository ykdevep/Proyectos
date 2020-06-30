-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: datawarehouse
-- ------------------------------------------------------
-- Server version	8.0.15

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
-- Temporary view structure for view `infoambloctiempo`
--

DROP TABLE IF EXISTS `infoambloctiempo`;
/*!50001 DROP VIEW IF EXISTS `infoambloctiempo`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `infoambloctiempo` AS SELECT 
 1 AS `DIA`,
 1 AS `MES`,
 1 AS `ANNO`,
 1 AS `HORA`,
 1 AS `MINUTO`,
 1 AS `DIOXAZUFRE`,
 1 AS `DIOXNITROGENO`,
 1 AS `MONOXCARBONO`,
 1 AS `MONOXNITROGENO`,
 1 AS `OXNITROGENO`,
 1 AS `OZONO`,
 1 AS `PM10`,
 1 AS `PM25`,
 1 AS `HUMRELATIVA`,
 1 AS `PRESIONATM`,
 1 AS `RADUVA`,
 1 AS `RADUVB`,
 1 AS `TEMPAMB`,
 1 AS `LATITUD`,
 1 AS `LONGITUD`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `varfisiologicas`
--

DROP TABLE IF EXISTS `varfisiologicas`;
/*!50001 DROP VIEW IF EXISTS `varfisiologicas`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `varfisiologicas` AS SELECT 
 1 AS `HR`,
 1 AS `TEMP`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `varfisiotiempo`
--

DROP TABLE IF EXISTS `varfisiotiempo`;
/*!50001 DROP VIEW IF EXISTS `varfisiotiempo`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `varfisiotiempo` AS SELECT 
 1 AS `DIA`,
 1 AS `MES`,
 1 AS `ANNO`,
 1 AS `HORA`,
 1 AS `MINUTO`,
 1 AS `HR`,
 1 AS `TEMP`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `varfisioinfoambloc`
--

DROP TABLE IF EXISTS `varfisioinfoambloc`;
/*!50001 DROP VIEW IF EXISTS `varfisioinfoambloc`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `varfisioinfoambloc` AS SELECT 
 1 AS `HR`,
 1 AS `TEMP`,
 1 AS `DIOXAZUFRE`,
 1 AS `DIOXNITROGENO`,
 1 AS `MONOXCARBONO`,
 1 AS `MONOXNITROGENO`,
 1 AS `OXNITROGENO`,
 1 AS `OZONO`,
 1 AS `PM10`,
 1 AS `PM25`,
 1 AS `HUMRELATIVA`,
 1 AS `PRESIONATM`,
 1 AS `RADUVA`,
 1 AS `RADUVB`,
 1 AS `TEMPAMB`,
 1 AS `LATITUD`,
 1 AS `LONGITUD`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `loctiempo`
--

DROP TABLE IF EXISTS `loctiempo`;
/*!50001 DROP VIEW IF EXISTS `loctiempo`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `loctiempo` AS SELECT 
 1 AS `DIA`,
 1 AS `MES`,
 1 AS `ANNO`,
 1 AS `HORA`,
 1 AS `MINUTO`,
 1 AS `LATITUD`,
 1 AS `LONGITUD`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `infoambloc`
--

DROP TABLE IF EXISTS `infoambloc`;
/*!50001 DROP VIEW IF EXISTS `infoambloc`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `infoambloc` AS SELECT 
 1 AS `DIOXAZUFRE`,
 1 AS `DIOXNITROGENO`,
 1 AS `MONOXCARBONO`,
 1 AS `MONOXNITROGENO`,
 1 AS `OXNITROGENO`,
 1 AS `OZONO`,
 1 AS `PM10`,
 1 AS `PM25`,
 1 AS `HUMRELATIVA`,
 1 AS `PRESIONATM`,
 1 AS `RADUVA`,
 1 AS `RADUVB`,
 1 AS `TEMPAMB`,
 1 AS `LATITUD`,
 1 AS `LONGITUD`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `infoambtiempo`
--

DROP TABLE IF EXISTS `infoambtiempo`;
/*!50001 DROP VIEW IF EXISTS `infoambtiempo`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `infoambtiempo` AS SELECT 
 1 AS `DIA`,
 1 AS `MES`,
 1 AS `ANNO`,
 1 AS `HORA`,
 1 AS `MINUTO`,
 1 AS `DIOXAZUFRE`,
 1 AS `DIOXNITROGENO`,
 1 AS `MONOXCARBONO`,
 1 AS `MONOXNITROGENO`,
 1 AS `OXNITROGENO`,
 1 AS `OZONO`,
 1 AS `PM10`,
 1 AS `PM25`,
 1 AS `HUMRELATIVA`,
 1 AS `PRESIONATM`,
 1 AS `RADUVA`,
 1 AS `RADUVB`,
 1 AS `TEMPAMB`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `localiz`
--

DROP TABLE IF EXISTS `localiz`;
/*!50001 DROP VIEW IF EXISTS `localiz`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `localiz` AS SELECT 
 1 AS `LATITUD`,
 1 AS `LONGITUD`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `varfisioloctiempo`
--

DROP TABLE IF EXISTS `varfisioloctiempo`;
/*!50001 DROP VIEW IF EXISTS `varfisioloctiempo`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `varfisioloctiempo` AS SELECT 
 1 AS `DIA`,
 1 AS `MES`,
 1 AS `ANNO`,
 1 AS `HORA`,
 1 AS `MINUTO`,
 1 AS `HR`,
 1 AS `TEMP`,
 1 AS `LATITUD`,
 1 AS `LONGITUD`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `varfisioloc`
--

DROP TABLE IF EXISTS `varfisioloc`;
/*!50001 DROP VIEW IF EXISTS `varfisioloc`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `varfisioloc` AS SELECT 
 1 AS `HR`,
 1 AS `TEMP`,
 1 AS `LATITUD`,
 1 AS `LONGITUD`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `varfisioinfoambloctiempo`
--

DROP TABLE IF EXISTS `varfisioinfoambloctiempo`;
/*!50001 DROP VIEW IF EXISTS `varfisioinfoambloctiempo`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `varfisioinfoambloctiempo` AS SELECT 
 1 AS `DIA`,
 1 AS `MES`,
 1 AS `ANNO`,
 1 AS `HORA`,
 1 AS `MINUTO`,
 1 AS `HR`,
 1 AS `TEMP`,
 1 AS `DIOXAZUFRE`,
 1 AS `DIOXNITROGENO`,
 1 AS `MONOXCARBONO`,
 1 AS `MONOXNITROGENO`,
 1 AS `OXNITROGENO`,
 1 AS `OZONO`,
 1 AS `PM10`,
 1 AS `PM25`,
 1 AS `HUMRELATIVA`,
 1 AS `PRESIONATM`,
 1 AS `RADUVA`,
 1 AS `RADUVB`,
 1 AS `TEMPAMB`,
 1 AS `LATITUD`,
 1 AS `LONGITUD`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `varfisioinfoamb`
--

DROP TABLE IF EXISTS `varfisioinfoamb`;
/*!50001 DROP VIEW IF EXISTS `varfisioinfoamb`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `varfisioinfoamb` AS SELECT 
 1 AS `HR`,
 1 AS `TEMP`,
 1 AS `DIOXAZUFRE`,
 1 AS `DIOXNITROGENO`,
 1 AS `MONOXCARBONO`,
 1 AS `MONOXNITROGENO`,
 1 AS `OXNITROGENO`,
 1 AS `OZONO`,
 1 AS `PM10`,
 1 AS `PM25`,
 1 AS `HUMRELATIVA`,
 1 AS `PRESIONATM`,
 1 AS `RADUVA`,
 1 AS `RADUVB`,
 1 AS `TEMPAMB`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `varfisioinfoambtiempo`
--

DROP TABLE IF EXISTS `varfisioinfoambtiempo`;
/*!50001 DROP VIEW IF EXISTS `varfisioinfoambtiempo`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `varfisioinfoambtiempo` AS SELECT 
 1 AS `DIA`,
 1 AS `MES`,
 1 AS `ANNO`,
 1 AS `HORA`,
 1 AS `MINUTO`,
 1 AS `HR`,
 1 AS `TEMP`,
 1 AS `DIOXAZUFRE`,
 1 AS `DIOXNITROGENO`,
 1 AS `MONOXCARBONO`,
 1 AS `MONOXNITROGENO`,
 1 AS `OXNITROGENO`,
 1 AS `OZONO`,
 1 AS `PM10`,
 1 AS `PM25`,
 1 AS `HUMRELATIVA`,
 1 AS `PRESIONATM`,
 1 AS `RADUVA`,
 1 AS `RADUVB`,
 1 AS `TEMPAMB`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `infoamb`
--

DROP TABLE IF EXISTS `infoamb`;
/*!50001 DROP VIEW IF EXISTS `infoamb`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `infoamb` AS SELECT 
 1 AS `DIOXAZUFRE`,
 1 AS `DIOXNITROGENO`,
 1 AS `MONOXCARBONO`,
 1 AS `MONOXNITROGENO`,
 1 AS `OXNITROGENO`,
 1 AS `OZONO`,
 1 AS `PM10`,
 1 AS `PM25`,
 1 AS `HUMRELATIVA`,
 1 AS `PRESIONATM`,
 1 AS `RADUVA`,
 1 AS `RADUVB`,
 1 AS `TEMPAMB`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `tiemp`
--

DROP TABLE IF EXISTS `tiemp`;
/*!50001 DROP VIEW IF EXISTS `tiemp`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `tiemp` AS SELECT 
 1 AS `DIA`,
 1 AS `MES`,
 1 AS `ANNO`,
 1 AS `HORA`,
 1 AS `MINUTO`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `infoambloctiempo`
--

/*!50001 DROP VIEW IF EXISTS `infoambloctiempo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`kike`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `infoambloctiempo` AS select `tiempo`.`DIA` AS `DIA`,`tiempo`.`MES` AS `MES`,`tiempo`.`ANNO` AS `ANNO`,`tiempo`.`HORA` AS `HORA`,`tiempo`.`MINUTO` AS `MINUTO`,`infoambiental`.`DIOXAZUFRE` AS `DIOXAZUFRE`,`infoambiental`.`DIOXNITROGENO` AS `DIOXNITROGENO`,`infoambiental`.`MONOXCARBONO` AS `MONOXCARBONO`,`infoambiental`.`MONOXNITROGENO` AS `MONOXNITROGENO`,`infoambiental`.`OXNITROGENO` AS `OXNITROGENO`,`infoambiental`.`OZONO` AS `OZONO`,`infoambiental`.`PM10` AS `PM10`,`infoambiental`.`PM25` AS `PM25`,`infoambiental`.`HUMRELATIVA` AS `HUMRELATIVA`,`infoambiental`.`PRESIONATM` AS `PRESIONATM`,`infoambiental`.`RADUVA` AS `RADUVA`,`infoambiental`.`RADUVB` AS `RADUVB`,`infoambiental`.`TEMPAMB` AS `TEMPAMB`,`localizacion`.`LATITUD` AS `LATITUD`,`localizacion`.`LONGITUD` AS `LONGITUD` from (((`infoambiental` join `comportamiento`) join `tiempo`) join `localizacion`) where ((`comportamiento`.`IDTIEMPO` = `tiempo`.`IDTIEMPO`) and (`comportamiento`.`IDINFOAMB` = `infoambiental`.`IDINFOAMB`) and (`comportamiento`.`IDMAPS` = `localizacion`.`IDMAPS`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `varfisiologicas`
--

/*!50001 DROP VIEW IF EXISTS `varfisiologicas`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`kike`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `varfisiologicas` AS select `e4hrtemp`.`HR` AS `HR`,`e4hrtemp`.`TEMP` AS `TEMP` from (`e4hrtemp` join `comportamiento`) where (`comportamiento`.`IDHR` = `e4hrtemp`.`IDHR`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `varfisiotiempo`
--

/*!50001 DROP VIEW IF EXISTS `varfisiotiempo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`kike`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `varfisiotiempo` AS select `tiempo`.`DIA` AS `DIA`,`tiempo`.`MES` AS `MES`,`tiempo`.`ANNO` AS `ANNO`,`tiempo`.`HORA` AS `HORA`,`tiempo`.`MINUTO` AS `MINUTO`,`e4hrtemp`.`HR` AS `HR`,`e4hrtemp`.`TEMP` AS `TEMP` from ((`e4hrtemp` join `comportamiento`) join `tiempo`) where ((`comportamiento`.`IDHR` = `e4hrtemp`.`IDHR`) and (`comportamiento`.`IDTIEMPO` = `tiempo`.`IDTIEMPO`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `varfisioinfoambloc`
--

/*!50001 DROP VIEW IF EXISTS `varfisioinfoambloc`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`kike`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `varfisioinfoambloc` AS select `e4hrtemp`.`HR` AS `HR`,`e4hrtemp`.`TEMP` AS `TEMP`,`infoambiental`.`DIOXAZUFRE` AS `DIOXAZUFRE`,`infoambiental`.`DIOXNITROGENO` AS `DIOXNITROGENO`,`infoambiental`.`MONOXCARBONO` AS `MONOXCARBONO`,`infoambiental`.`MONOXNITROGENO` AS `MONOXNITROGENO`,`infoambiental`.`OXNITROGENO` AS `OXNITROGENO`,`infoambiental`.`OZONO` AS `OZONO`,`infoambiental`.`PM10` AS `PM10`,`infoambiental`.`PM25` AS `PM25`,`infoambiental`.`HUMRELATIVA` AS `HUMRELATIVA`,`infoambiental`.`PRESIONATM` AS `PRESIONATM`,`infoambiental`.`RADUVA` AS `RADUVA`,`infoambiental`.`RADUVB` AS `RADUVB`,`infoambiental`.`TEMPAMB` AS `TEMPAMB`,`localizacion`.`LATITUD` AS `LATITUD`,`localizacion`.`LONGITUD` AS `LONGITUD` from (((`e4hrtemp` join `comportamiento`) join `localizacion`) join `infoambiental`) where ((`comportamiento`.`IDMAPS` = `localizacion`.`IDMAPS`) and (`comportamiento`.`IDHR` = `e4hrtemp`.`IDHR`) and (`comportamiento`.`IDINFOAMB` = `infoambiental`.`IDINFOAMB`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `loctiempo`
--

/*!50001 DROP VIEW IF EXISTS `loctiempo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`kike`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `loctiempo` AS select `tiempo`.`DIA` AS `DIA`,`tiempo`.`MES` AS `MES`,`tiempo`.`ANNO` AS `ANNO`,`tiempo`.`HORA` AS `HORA`,`tiempo`.`MINUTO` AS `MINUTO`,`localizacion`.`LATITUD` AS `LATITUD`,`localizacion`.`LONGITUD` AS `LONGITUD` from ((`tiempo` join `comportamiento`) join `localizacion`) where ((`comportamiento`.`IDMAPS` = `localizacion`.`IDMAPS`) and (`comportamiento`.`IDTIEMPO` = `tiempo`.`IDTIEMPO`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `infoambloc`
--

/*!50001 DROP VIEW IF EXISTS `infoambloc`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`kike`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `infoambloc` AS select `infoambiental`.`DIOXAZUFRE` AS `DIOXAZUFRE`,`infoambiental`.`DIOXNITROGENO` AS `DIOXNITROGENO`,`infoambiental`.`MONOXCARBONO` AS `MONOXCARBONO`,`infoambiental`.`MONOXNITROGENO` AS `MONOXNITROGENO`,`infoambiental`.`OXNITROGENO` AS `OXNITROGENO`,`infoambiental`.`OZONO` AS `OZONO`,`infoambiental`.`PM10` AS `PM10`,`infoambiental`.`PM25` AS `PM25`,`infoambiental`.`HUMRELATIVA` AS `HUMRELATIVA`,`infoambiental`.`PRESIONATM` AS `PRESIONATM`,`infoambiental`.`RADUVA` AS `RADUVA`,`infoambiental`.`RADUVB` AS `RADUVB`,`infoambiental`.`TEMPAMB` AS `TEMPAMB`,`localizacion`.`LATITUD` AS `LATITUD`,`localizacion`.`LONGITUD` AS `LONGITUD` from ((`infoambiental` join `comportamiento`) join `localizacion`) where ((`comportamiento`.`IDINFOAMB` = `infoambiental`.`IDINFOAMB`) and (`comportamiento`.`IDMAPS` = `localizacion`.`IDMAPS`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `infoambtiempo`
--

/*!50001 DROP VIEW IF EXISTS `infoambtiempo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`kike`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `infoambtiempo` AS select `tiempo`.`DIA` AS `DIA`,`tiempo`.`MES` AS `MES`,`tiempo`.`ANNO` AS `ANNO`,`tiempo`.`HORA` AS `HORA`,`tiempo`.`MINUTO` AS `MINUTO`,`infoambiental`.`DIOXAZUFRE` AS `DIOXAZUFRE`,`infoambiental`.`DIOXNITROGENO` AS `DIOXNITROGENO`,`infoambiental`.`MONOXCARBONO` AS `MONOXCARBONO`,`infoambiental`.`MONOXNITROGENO` AS `MONOXNITROGENO`,`infoambiental`.`OXNITROGENO` AS `OXNITROGENO`,`infoambiental`.`OZONO` AS `OZONO`,`infoambiental`.`PM10` AS `PM10`,`infoambiental`.`PM25` AS `PM25`,`infoambiental`.`HUMRELATIVA` AS `HUMRELATIVA`,`infoambiental`.`PRESIONATM` AS `PRESIONATM`,`infoambiental`.`RADUVA` AS `RADUVA`,`infoambiental`.`RADUVB` AS `RADUVB`,`infoambiental`.`TEMPAMB` AS `TEMPAMB` from ((`infoambiental` join `comportamiento`) join `tiempo`) where ((`comportamiento`.`IDINFOAMB` = `infoambiental`.`IDINFOAMB`) and (`comportamiento`.`IDTIEMPO` = `tiempo`.`IDTIEMPO`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `localiz`
--

/*!50001 DROP VIEW IF EXISTS `localiz`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`kike`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `localiz` AS select `localizacion`.`LATITUD` AS `LATITUD`,`localizacion`.`LONGITUD` AS `LONGITUD` from (`localizacion` join `comportamiento`) where (`comportamiento`.`IDMAPS` = `localizacion`.`IDMAPS`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `varfisioloctiempo`
--

/*!50001 DROP VIEW IF EXISTS `varfisioloctiempo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`kike`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `varfisioloctiempo` AS select `tiempo`.`DIA` AS `DIA`,`tiempo`.`MES` AS `MES`,`tiempo`.`ANNO` AS `ANNO`,`tiempo`.`HORA` AS `HORA`,`tiempo`.`MINUTO` AS `MINUTO`,`e4hrtemp`.`HR` AS `HR`,`e4hrtemp`.`TEMP` AS `TEMP`,`localizacion`.`LATITUD` AS `LATITUD`,`localizacion`.`LONGITUD` AS `LONGITUD` from (((`e4hrtemp` join `comportamiento`) join `tiempo`) join `localizacion`) where ((`comportamiento`.`IDTIEMPO` = `tiempo`.`IDTIEMPO`) and (`comportamiento`.`IDHR` = `e4hrtemp`.`IDHR`) and (`comportamiento`.`IDMAPS` = `localizacion`.`IDMAPS`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `varfisioloc`
--

/*!50001 DROP VIEW IF EXISTS `varfisioloc`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`kike`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `varfisioloc` AS select `e4hrtemp`.`HR` AS `HR`,`e4hrtemp`.`TEMP` AS `TEMP`,`localizacion`.`LATITUD` AS `LATITUD`,`localizacion`.`LONGITUD` AS `LONGITUD` from ((`e4hrtemp` join `comportamiento`) join `localizacion`) where ((`comportamiento`.`IDMAPS` = `localizacion`.`IDMAPS`) and (`comportamiento`.`IDHR` = `e4hrtemp`.`IDHR`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `varfisioinfoambloctiempo`
--

/*!50001 DROP VIEW IF EXISTS `varfisioinfoambloctiempo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`kike`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `varfisioinfoambloctiempo` AS select `tiempo`.`DIA` AS `DIA`,`tiempo`.`MES` AS `MES`,`tiempo`.`ANNO` AS `ANNO`,`tiempo`.`HORA` AS `HORA`,`tiempo`.`MINUTO` AS `MINUTO`,`e4hrtemp`.`HR` AS `HR`,`e4hrtemp`.`TEMP` AS `TEMP`,`infoambiental`.`DIOXAZUFRE` AS `DIOXAZUFRE`,`infoambiental`.`DIOXNITROGENO` AS `DIOXNITROGENO`,`infoambiental`.`MONOXCARBONO` AS `MONOXCARBONO`,`infoambiental`.`MONOXNITROGENO` AS `MONOXNITROGENO`,`infoambiental`.`OXNITROGENO` AS `OXNITROGENO`,`infoambiental`.`OZONO` AS `OZONO`,`infoambiental`.`PM10` AS `PM10`,`infoambiental`.`PM25` AS `PM25`,`infoambiental`.`HUMRELATIVA` AS `HUMRELATIVA`,`infoambiental`.`PRESIONATM` AS `PRESIONATM`,`infoambiental`.`RADUVA` AS `RADUVA`,`infoambiental`.`RADUVB` AS `RADUVB`,`infoambiental`.`TEMPAMB` AS `TEMPAMB`,`localizacion`.`LATITUD` AS `LATITUD`,`localizacion`.`LONGITUD` AS `LONGITUD` from ((((`infoambiental` join `comportamiento`) join `e4hrtemp`) join `tiempo`) join `localizacion`) where ((`comportamiento`.`IDTIEMPO` = `tiempo`.`IDTIEMPO`) and (`comportamiento`.`IDINFOAMB` = `infoambiental`.`IDINFOAMB`) and (`comportamiento`.`IDMAPS` = `localizacion`.`IDMAPS`) and (`comportamiento`.`IDHR` = `e4hrtemp`.`IDHR`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `varfisioinfoamb`
--

/*!50001 DROP VIEW IF EXISTS `varfisioinfoamb`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`kike`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `varfisioinfoamb` AS select `e4hrtemp`.`HR` AS `HR`,`e4hrtemp`.`TEMP` AS `TEMP`,`infoambiental`.`DIOXAZUFRE` AS `DIOXAZUFRE`,`infoambiental`.`DIOXNITROGENO` AS `DIOXNITROGENO`,`infoambiental`.`MONOXCARBONO` AS `MONOXCARBONO`,`infoambiental`.`MONOXNITROGENO` AS `MONOXNITROGENO`,`infoambiental`.`OXNITROGENO` AS `OXNITROGENO`,`infoambiental`.`OZONO` AS `OZONO`,`infoambiental`.`PM10` AS `PM10`,`infoambiental`.`PM25` AS `PM25`,`infoambiental`.`HUMRELATIVA` AS `HUMRELATIVA`,`infoambiental`.`PRESIONATM` AS `PRESIONATM`,`infoambiental`.`RADUVA` AS `RADUVA`,`infoambiental`.`RADUVB` AS `RADUVB`,`infoambiental`.`TEMPAMB` AS `TEMPAMB` from ((`e4hrtemp` join `comportamiento`) join `infoambiental`) where ((`comportamiento`.`IDHR` = `e4hrtemp`.`IDHR`) and (`comportamiento`.`IDINFOAMB` = `infoambiental`.`IDINFOAMB`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `varfisioinfoambtiempo`
--

/*!50001 DROP VIEW IF EXISTS `varfisioinfoambtiempo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`kike`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `varfisioinfoambtiempo` AS select `tiempo`.`DIA` AS `DIA`,`tiempo`.`MES` AS `MES`,`tiempo`.`ANNO` AS `ANNO`,`tiempo`.`HORA` AS `HORA`,`tiempo`.`MINUTO` AS `MINUTO`,`e4hrtemp`.`HR` AS `HR`,`e4hrtemp`.`TEMP` AS `TEMP`,`infoambiental`.`DIOXAZUFRE` AS `DIOXAZUFRE`,`infoambiental`.`DIOXNITROGENO` AS `DIOXNITROGENO`,`infoambiental`.`MONOXCARBONO` AS `MONOXCARBONO`,`infoambiental`.`MONOXNITROGENO` AS `MONOXNITROGENO`,`infoambiental`.`OXNITROGENO` AS `OXNITROGENO`,`infoambiental`.`OZONO` AS `OZONO`,`infoambiental`.`PM10` AS `PM10`,`infoambiental`.`PM25` AS `PM25`,`infoambiental`.`HUMRELATIVA` AS `HUMRELATIVA`,`infoambiental`.`PRESIONATM` AS `PRESIONATM`,`infoambiental`.`RADUVA` AS `RADUVA`,`infoambiental`.`RADUVB` AS `RADUVB`,`infoambiental`.`TEMPAMB` AS `TEMPAMB` from (((`e4hrtemp` join `comportamiento`) join `tiempo`) join `infoambiental`) where ((`comportamiento`.`IDTIEMPO` = `tiempo`.`IDTIEMPO`) and (`comportamiento`.`IDHR` = `e4hrtemp`.`IDHR`) and (`comportamiento`.`IDINFOAMB` = `infoambiental`.`IDINFOAMB`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `infoamb`
--

/*!50001 DROP VIEW IF EXISTS `infoamb`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`kike`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `infoamb` AS select `infoambiental`.`DIOXAZUFRE` AS `DIOXAZUFRE`,`infoambiental`.`DIOXNITROGENO` AS `DIOXNITROGENO`,`infoambiental`.`MONOXCARBONO` AS `MONOXCARBONO`,`infoambiental`.`MONOXNITROGENO` AS `MONOXNITROGENO`,`infoambiental`.`OXNITROGENO` AS `OXNITROGENO`,`infoambiental`.`OZONO` AS `OZONO`,`infoambiental`.`PM10` AS `PM10`,`infoambiental`.`PM25` AS `PM25`,`infoambiental`.`HUMRELATIVA` AS `HUMRELATIVA`,`infoambiental`.`PRESIONATM` AS `PRESIONATM`,`infoambiental`.`RADUVA` AS `RADUVA`,`infoambiental`.`RADUVB` AS `RADUVB`,`infoambiental`.`TEMPAMB` AS `TEMPAMB` from (`infoambiental` join `comportamiento`) where (`comportamiento`.`IDINFOAMB` = `infoambiental`.`IDINFOAMB`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `tiemp`
--

/*!50001 DROP VIEW IF EXISTS `tiemp`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`kike`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `tiemp` AS select `tiempo`.`DIA` AS `DIA`,`tiempo`.`MES` AS `MES`,`tiempo`.`ANNO` AS `ANNO`,`tiempo`.`HORA` AS `HORA`,`tiempo`.`MINUTO` AS `MINUTO` from (`tiempo` join `comportamiento`) where (`comportamiento`.`IDTIEMPO` = `tiempo`.`IDTIEMPO`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-29 22:28:31
