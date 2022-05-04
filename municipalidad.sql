-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: municipalidad
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `USUARIO` varchar(45) NOT NULL,
  `PASSWORD` varchar(45) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boleta_venta`
--

DROP TABLE IF EXISTS `boleta_venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `boleta_venta` (
  `NUM_BOLETA` varchar(45) NOT NULL,
  `LOTE` varchar(45) NOT NULL,
  `FECHA` varchar(45) NOT NULL,
  `ESTADO` varchar(45) NOT NULL,
  `CANTIDAD` float NOT NULL,
  `PRECIO` float NOT NULL,
  `TOTAL` float NOT NULL,
  `NOMBRE_CLIENTE` varchar(45) NOT NULL,
  `RUC_CLIENTE` varchar(45) NOT NULL,
  PRIMARY KEY (`NUM_BOLETA`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boleta_venta`
--

LOCK TABLES `boleta_venta` WRITE;
/*!40000 ALTER TABLE `boleta_venta` DISABLE KEYS */;
INSERT INTO `boleta_venta` VALUES ('1','0001','30/01/2021','PAGADO',1,6.8,6.8,'Flores S.A.C','20051271245'),('2','0002','30/01/2021','PAGADO',2,6.8,13.6,'Jardin S.A.C','20041245185'),('3','0002','30/01/2021','{POR PAGAR}',1,6.8,6.8,'Sulivan S.A.C','20030445185');
/*!40000 ALTER TABLE `boleta_venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compras`
--

DROP TABLE IF EXISTS `compras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compras` (
  `ID_COMPRA` varchar(45) NOT NULL,
  `ID_PROVEEDOR` varchar(45) NOT NULL,
  `FECHA` varchar(45) NOT NULL,
  `PRODUCTO` varchar(45) NOT NULL,
  `PRECIO` float NOT NULL,
  `CANTIDAD` float NOT NULL,
  `TOTAL` float NOT NULL,
  PRIMARY KEY (`ID_COMPRA`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compras`
--

LOCK TABLES `compras` WRITE;
/*!40000 ALTER TABLE `compras` DISABLE KEYS */;
INSERT INTO `compras` VALUES ('COMPRA-001','PROV-001','02/07/2021','MICROORGANISMO',18,2,36);
/*!40000 ALTER TABLE `compras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventario`
--

DROP TABLE IF EXISTS `inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventario` (
  `ID_INV` varchar(45) NOT NULL,
  `ID_COMPRA` varchar(45) NOT NULL,
  `AREA` varchar(45) NOT NULL,
  `TIPO_RECURSO` varchar(45) NOT NULL,
  `NOMBRE_RECURSO` varchar(45) NOT NULL,
  `UNIDAD` varchar(45) NOT NULL,
  `CANTIDAD` int NOT NULL,
  `DESCRIPCION` longtext NOT NULL,
  PRIMARY KEY (`ID_INV`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventario`
--

LOCK TABLES `inventario` WRITE;
/*!40000 ALTER TABLE `inventario` DISABLE KEYS */;
INSERT INTO `inventario` VALUES ('INV-001','COMPRA-001','Recepción_MP','OTROS','Tri Movil ','{NO APLICA}',2,'Medio de transporte para recoleccion de residuos para ser transportados hacia la planta de valortización');
/*!40000 ALTER TABLE `inventario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materia_prima`
--

DROP TABLE IF EXISTS `materia_prima`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materia_prima` (
  `ID` varchar(45) NOT NULL,
  `AREA` varchar(45) NOT NULL,
  `FECHA` varchar(45) NOT NULL,
  `HORA_ENTRADA` time NOT NULL,
  `ZONA` varchar(45) NOT NULL,
  `LOTE` varchar(45) NOT NULL,
  `PESO` float NOT NULL,
  `ENCARGADO` longtext NOT NULL,
  `SOPORTE` longtext NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materia_prima`
--

LOCK TABLES `materia_prima` WRITE;
/*!40000 ALTER TABLE `materia_prima` DISABLE KEYS */;
INSERT INTO `materia_prima` VALUES ('0001','Recepción_MP','01/12/2020','08:00:00','Zona 2','MP-001',25,'Operario 1','Operario 3 '),('0002','Recepción_MP','1/12/2020','08:00:00','Zona 4','MP-001',85,'Sr Jorge','Operario 3 y  Operario 4'),('0003','Recepción_MP','1/12/2020','08:15:00','Zona 5','MP-001',81,'Sr Jorge','Operario 3 y  Operario 4'),('0004','Recepción_MP','1/12/2020','08:30:00','Zona 2','MP-001',80,'Sr Jorge','Operario 3 y  Operario 4'),('0005','Recepción_MP','1/12/2020','08:35:00','Zona 4','MP-001',47.5,'Sr Juan','Operario 1 y Operario 2 '),('0006','Recepción_MP','1/12/2020','08:45:00','Zona 2','MP-001',86,'Sr Jorge','Operario 3 y  Operario 4'),('0007','Recepción_MP','1/12/2020','09:00:00','Zona 1','MP-001',38.95,'Sr Juan','Operario 1 y Operario 2 '),('0008','Recepción_MP','1/12/2020','09:15:00','Zona 3','MP-001',83.7,'Sr Jorge','Operario 3 y  Operario 4'),('0009','Recepción_MP','1/12/2020','12:00:00','Zona 5','MP-001',67.4675,'Sr Juan','Operario 1 y Operario 2 '),('0010','Recepción_MP','1/12/2020','12:15:00','Zona 4','MP-001',84.1,'Sr Jorge','Operario 3 y  Operario 4'),('0011','Recepción_MP','1/12/2020','12:30:00','Zona 2','MP-001',57.4675,'Sr Juan','Operario 1 y Operario 2 '),('0012','Recepción_MP','1/12/2020','12:45:00','Zona 5','MP-001',84.5,'Sr Jorge','Operario 3 y  Operario 4'),('0013','Recepción_MP','1/12/2020','15:24:00','Zona 5','MP-001',47.4675,'Sr Juan','Operario 1 y Operario 2 '),('0014','Recepción_MP','1/12/2020','15:30:00','Zona 1','MP-001',84.5,'Sr Jorge','Operario 3 y  Operario 4'),('0015','Recepción_MP','1/12/2020','15:31:00','Zona 2','MP-001',84.7,'Sr Jorge','Operario 3 y  Operario 4'),('0016','Recepción_MP','1/12/2020','15:37:00','Zona 5','MP-001',84.9,'Sr Jorge','Operario 3 y  Operario 4'),('0017','Recepción_MP','1/12/2020','15:45:00','Zona 2','MP-001',85.1,'Sr Jorge','Operario 3 y  Operario 4'),('0018','Recepción_MP','1/12/2020','15:50:00','Zona 1','MP-001',39.4675,'Sr Juan','Operario 1 y Operario 2 '),('0019','Recepción_MP','1/12/2020','16:15:00','Zona 3','MP-001',84.9,'Sr Jorge','Operario 3 y  Operario 4'),('0020','Recepción_MP','1/12/2020','17:10:00','Zona 2','MP-001',85.1,'Sr Jorge','Operario 3 y  Operario 4'),('0021','Recepción_MP','2/12/2020','08:00:00','Zona 3','MP-002',74.5699,'Sr Juan','Operario 1 y Operario 3'),('0022','Recepción_MP','2/12/2020','08:00:00','Zona 2','MP-002',74.672,'Sr Jorge','Operario 3 y  Operario 4'),('0023','Recepción_MP','2/12/2020','08:15:00','Zona 5','MP-002',74.7741,'Sr Jorge','Operario 3 y  Operario 4'),('0024','Recepción_MP','2/12/2020','08:30:00','Zona 4','MP-002',74.8762,'Sr Jorge','Operario 3 y  Operario 4'),('0025','Recepción_MP','2/12/2020','08:35:00','Zona 3','MP-002',74.9784,'Sr Juan','Operario 1 y Operario 3'),('0026','Recepción_MP','2/12/2020','08:45:00','Zona 3','MP-002',75.0805,'Sr Jorge','Operario 3 y  Operario 5'),('0027','Recepción_MP','2/12/2020','09:00:00','Zona 1','MP-002',75.1826,'Sr Juan','Operario 1 y Operario 3'),('0028','Recepción_MP','2/12/2020','09:15:00','Zona 2','MP-002',75.2847,'Sr Jorge','Operario 3 y  Operario 5'),('0029','Recepción_MP','2/12/2020','12:00:00','Zona 4','MP-002',75.3868,'Sr Juan','Operario 1 y Operario 3'),('0030','Recepción_MP','2/12/2020','12:15:00','Zona 4','MP-002',75.4889,'Sr Jorge','Operario 3 y  Operario 5'),('0031','Recepción_MP','2/12/2020','12:30:00','Zona 1','MP-002',75.591,'Sr Juan','Operario 1 y Operario 3'),('0032','Recepción_MP','2/12/2020','12:45:00','Zona 1','MP-002',75.6931,'Sr Jorge','Operario 3 y  Operario 5'),('0033','Recepción_MP','2/12/2020','15:24:00','Zona 2','MP-002',75.7953,'Sr Juan','Operario 1 y Operario 3'),('0034','Recepción_MP','2/12/2020','15:30:00','Zona 3','MP-002',75.8974,'Sr Jorge','Operario 3 y  Operario 4'),('0035','Recepción_MP','2/12/2020','15:31:00','Zona 5','MP-002',75.9995,'Sr Jorge','Operario 3 y  Operario 4'),('0036','Recepción_MP','2/12/2020','15:37:00','Zona 3','MP-002',76.1016,'Sr Jorge','Operario 3 y  Operario 4'),('0037','Recepción_MP','2/12/2020','15:45:00','Zona 1','MP-002',76.2037,'Sr Jorge','Operario 3 y  Operario 4'),('0038','Recepción_MP','2/12/2020','15:50:00','Zona 1','MP-002',76.3058,'Sr Juan','Operario 1 y Operario 3'),('0039','Recepción_MP','2/12/2020','16:15:00','Zona 3','MP-002',76.4079,'Sr Jorge','Operario 3 y  Operario 4'),('0040','Recepción_MP','2/12/2020','17:10:00','Zona 4','MP-002',76.51,'Sr Jorge','Operario 3 y  Operario 4'),('0041','Recepción_MP','5/12/2020','08:00:00','Zona 2','MP-003',76.6122,'Sr Juan','Operario 1 y Operario 4'),('0042','Recepción_MP','5/12/2020','08:00:00','Zona 1','MP-003',76.7143,'Sr Jorge','Operario 3 y  Operario 4'),('0043','Recepción_MP','5/12/2020','08:15:00','Zona 1','MP-003',76.8164,'Sr Jorge','Operario 3 y  Operario 4'),('0044','Recepción_MP','5/12/2020','08:30:00','Zona 5','MP-003',76.9185,'Sr Jorge','Operario 3 y  Operario 4'),('0045','Recepción_MP','5/12/2020','08:35:00','Zona 4','MP-003',77.0206,'Sr Juan','Operario 1 y Operario 4'),('0046','Recepción_MP','5/12/2020','08:45:00','Zona 1','MP-003',77.1227,'Sr Jorge','Operario 3 y  Operario 6'),('0047','Recepción_MP','5/12/2020','09:00:00','Zona 4','MP-003',77.2248,'Sr Juan','Operario 1 y Operario 4'),('0048','Recepción_MP','5/12/2020','09:15:00','Zona 4','MP-003',77.3269,'Sr Jorge','Operario 3 y  Operario 6'),('0049','Recepción_MP','5/12/2020','12:00:00','Zona 1','MP-003',77.4291,'Sr Juan','Operario 1 y Operario 4'),('0050','Recepción_MP','5/12/2020','12:15:00','Zona 4','MP-003',77.5312,'Sr Jorge','Operario 3 y  Operario 6'),('0051','Recepción_MP','5/12/2020','12:30:00','Zona 5','MP-003',77.6333,'Sr Juan','Operario 1 y Operario 4'),('0052','Recepción_MP','5/12/2020','12:45:00','Zona 5','MP-003',77.7354,'Sr Jorge','Operario 3 y  Operario 6'),('0053','Recepción_MP','5/12/2020','15:24:00','Zona 5','MP-003',77.8375,'Sr Juan','Operario 1 y Operario 4'),('0054','Recepción_MP','5/12/2020','15:30:00','Zona 4','MP-003',77.9396,'Sr Jorge','Operario 3 y  Operario 4'),('0055','Recepción_MP','5/12/2020','15:31:00','Zona 1','MP-003',78.0417,'Sr Jorge','Operario 3 y  Operario 4'),('0056','Recepción_MP','5/12/2020','15:37:00','Zona 4','MP-003',78.1438,'Sr Jorge','Operario 3 y  Operario 4'),('0057','Recepción_MP','5/12/2020','15:45:00','Zona 2','MP-003',78.2459,'Sr Jorge','Operario 3 y  Operario 4'),('0058','Recepción_MP','5/12/2020','15:50:00','Zona 3','MP-003',78.3481,'Sr Juan','Operario 1 y Operario 4'),('0059','Recepción_MP','5/12/2020','16:15:00','Zona 2','MP-003',78.4502,'Sr Jorge','Operario 3 y  Operario 4'),('0060','Recepción_MP','5/12/2020','17:10:00','Zona 5','MP-003',78.5523,'Sr Jorge','Operario 3 y  Operario 4'),('0061','Recepción_MP','7/12/2020','08:00:00','Zona 4','MP-004',78.6544,'Sr Juan','Operario 1 y Operario 5'),('0062','Recepción_MP','7/12/2020','08:00:00','Zona 5','MP-004',78.7565,'Sr Jorge','Operario 3 y  Operario 4'),('0063','Recepción_MP','7/12/2020','08:15:00','Zona 4','MP-004',78.8586,'Sr Jorge','Operario 3 y  Operario 4'),('0064','Recepción_MP','7/12/2020','08:30:00','Zona 3','MP-004',78.9607,'Sr Jorge','Operario 3 y  Operario 4'),('0065','Recepción_MP','7/12/2020','08:35:00','Zona 3','MP-004',79.0629,'Sr Juan','Operario 1 y Operario 5'),('0066','Recepción_MP','7/12/2020','08:45:00','Zona 3','MP-004',79.165,'Sr Jorge','Operario 3 y  Operario 7'),('0067','Recepción_MP','7/12/2020','09:00:00','Zona 2','MP-004',79.2671,'Sr Juan','Operario 1 y Operario 5'),('0068','Recepción_MP','7/12/2020','09:15:00','Zona 4','MP-004',79.3692,'Sr Jorge','Operario 3 y  Operario 7'),('0069','Recepción_MP','7/12/2020','12:00:00','Zona 2','MP-004',79.4713,'Sr Juan','Operario 1 y Operario 5'),('0070','Recepción_MP','7/12/2020','12:15:00','Zona 4','MP-004',79.5734,'Sr Jorge','Operario 3 y  Operario 7'),('0071','Recepción_MP','7/12/2020','12:30:00','Zona 1','MP-004',79.6755,'Sr Juan','Operario 1 y Operario 5'),('0072','Recepción_MP','7/12/2020','12:45:00','Zona 5','MP-004',79.7776,'Sr Jorge','Operario 3 y  Operario 7'),('0073','Recepción_MP','7/12/2020','15:24:00','Zona 3','MP-004',79.8798,'Sr Juan','Operario 1 y Operario 5'),('0074','Recepción_MP','7/12/2020','15:30:00','Zona 4','MP-004',79.9819,'Sr Jorge','Operario 3 y  Operario 4'),('0075','Recepción_MP','7/12/2020','15:31:00','Zona 4','MP-004',80.084,'Sr Jorge','Operario 3 y  Operario 4'),('0076','Recepción_MP','7/12/2020','15:37:00','Zona 2','MP-004',80.1861,'Sr Jorge','Operario 3 y  Operario 4'),('0077','Recepción_MP','7/12/2020','15:45:00','Zona 4','MP-004',80.2882,'Sr Jorge','Operario 3 y  Operario 4'),('0078','Recepción_MP','7/12/2020','15:50:00','Zona 5','MP-004',80.3903,'Sr Juan','Operario 1 y Operario 5'),('0079','Recepción_MP','7/12/2020','16:15:00','Zona 4','MP-004',80.4924,'Sr Jorge','Operario 3 y  Operario 4'),('0080','Recepción_MP','7/12/2020','17:10:00','Zona 3','MP-004',80.5945,'Sr Jorge','Operario 3 y  Operario 4'),('0081','Recepción_MP','9/12/2020','08:00:00','Zona 1','MP-005',80.6966,'Sr Juan','Operario 1 y Operario 6'),('0082','Recepción_MP','9/12/2020','08:00:00','Zona 1','MP-005',80.7988,'Sr Jorge','Operario 3 y  Operario 4'),('0083','Recepción_MP','9/12/2020','08:15:00','Zona 5','MP-005',80.9009,'Sr Jorge','Operario 3 y  Operario 4'),('0084','Recepción_MP','9/12/2020','08:30:00','Zona 4','MP-005',81.003,'Sr Jorge','Operario 3 y  Operario 4'),('0085','Recepción_MP','9/12/2020','08:35:00','Zona 5','MP-005',81.1051,'Sr Juan','Operario 1 y Operario 6'),('0086','Recepción_MP','9/12/2020','08:45:00','Zona 3','MP-005',81.2072,'Sr Jorge','Operario 3 y  Operario 8'),('0087','Recepción_MP','9/12/2020','09:00:00','Zona 2','MP-005',81.3093,'Sr Juan','Operario 1 y Operario 6'),('0088','Recepción_MP','9/12/2020','09:15:00','Zona 5','MP-005',81.4114,'Sr Jorge','Operario 3 y  Operario 8'),('0089','Recepción_MP','9/12/2020','12:00:00','Zona 4','MP-005',81.5135,'Sr Juan','Operario 1 y Operario 6'),('0090','Recepción_MP','9/12/2020','12:15:00','Zona 2','MP-005',81.6157,'Sr Jorge','Operario 3 y  Operario 8'),('0091','Recepción_MP','9/12/2020','12:30:00','Zona 4','MP-005',81.7178,'Sr Juan','Operario 1 y Operario 6'),('0092','Recepción_MP','9/12/2020','12:45:00','Zona 2','MP-005',81.8199,'Sr Jorge','Operario 3 y  Operario 8'),('0093','Recepción_MP','9/12/2020','15:24:00','Zona 4','MP-005',81.922,'Sr Juan','Operario 1 y Operario 6'),('0094','Recepción_MP','9/12/2020','15:30:00','Zona 4','MP-005',82.0241,'Sr Jorge','Operario 3 y  Operario 4'),('0095','Recepción_MP','9/12/2020','15:31:00','Zona 4','MP-005',82.1262,'Sr Jorge','Operario 3 y  Operario 4'),('0096','Recepción_MP','9/12/2020','15:37:00','Zona 2','MP-005',82.2283,'Sr Jorge','Operario 3 y  Operario 4'),('0097','Recepción_MP','9/12/2020','15:45:00','Zona 5','MP-005',82.3304,'Sr Jorge','Operario 3 y  Operario 4'),('0098','Recepción_MP','9/12/2020','15:50:00','Zona 2','MP-005',82.4326,'Sr Juan','Operario 1 y Operario 6'),('0099','Recepción_MP','9/12/2020','16:15:00','Zona 1','MP-005',82.5347,'Sr Jorge','Operario 3 y  Operario 4'),('0100','Recepción_MP','9/12/2020','17:10:00','Zona 1','MP-005',82.6368,'Sr Jorge','Operario 3 y  Operario 4');
/*!40000 ALTER TABLE `materia_prima` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal`
--

DROP TABLE IF EXISTS `personal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal` (
  `ID_PERSONAL` varchar(45) NOT NULL,
  `NOMBRE` varchar(45) NOT NULL,
  `APELLIDO` varchar(45) NOT NULL,
  `FECHA_NACIMIENTO` varchar(45) NOT NULL,
  `FECHA_INGRESO` varchar(45) NOT NULL,
  `PUESTO` varchar(45) NOT NULL,
  `EDAD` int NOT NULL,
  `A_EXPERIENCIA` int NOT NULL,
  `CORREO` varchar(45) NOT NULL,
  `TELEFONO` int NOT NULL,
  `SALARIO_MENSUAL` int NOT NULL,
  PRIMARY KEY (`ID_PERSONAL`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal`
--

LOCK TABLES `personal` WRITE;
/*!40000 ALTER TABLE `personal` DISABLE KEYS */;
INSERT INTO `personal` VALUES ('P-0001','Juan ','Moran','05/12/1980','01/04/2021','Operario',39,4,'juan.moran@gmail.com',95074124,930),('P-0002','Andy','Cordova','01/12/1995','03/12/2020','Operario',25,1,'a.cordova@gmail.com',998997511,930),('P-0003','Juan','Delgado','02/09/1998','01/12/2020','Operario',22,2,'j.delgado@gmail.com',917997511,930),('P-0004','Julio','Ramirez','01/08/1997','11/12/2020','Operario',24,3,'j.ramirez@gmail.com',917997515,930),('P-0005','Kevin','Perez','30/07/1992','29/11/2019','Operario',29,6,'k.perez@gmail.com',917997510,930),('P-0006','Kenny','Morales','17/07/1991','29/11/2019','Operario',30,9,'k.morales@gmail.com',928997410,930),('P-0007','Luisa ','Perales','28/06/1990','29/11/2019','Ingeniero',31,9,'l.perales@gmail.com',987697410,1200),('P-0008','Luis','Carbajal','02/06/1989','29/11/2019','Ingeniero',32,10,'l.carbajal@gmail.com',987487410,1200),('P-0009','Pedro','Orozco','04/06/1987','29/11/2019','Ingeniero',34,12,'P.orozco@gmail.com',987484510,1200),('P-0010','Juan','Alcacer','04/06/1981','29/11/2019','Chofer',40,12,'j.alacer@gmail.com',984784451,930);
/*!40000 ALTER TABLE `personal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto_en_proceso`
--

DROP TABLE IF EXISTS `producto_en_proceso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto_en_proceso` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `AREA` varchar(45) NOT NULL,
  `FECHA` varchar(45) NOT NULL,
  `HORA_ENTRADA` time NOT NULL,
  `NRO_CAMA` varchar(45) NOT NULL,
  `LOTE` varchar(45) NOT NULL,
  `PESO` float NOT NULL,
  `CANT_MICROORGANISMO` float NOT NULL,
  `TEMPERATURA` int NOT NULL,
  `ENCARGADO` varchar(45) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto_en_proceso`
--

LOCK TABLES `producto_en_proceso` WRITE;
/*!40000 ALTER TABLE `producto_en_proceso` DISABLE KEYS */;
INSERT INTO `producto_en_proceso` VALUES (1,'Producción','03/12/2021','08:00:00','Cama 3','PP-001-111521',35,45,12,'Sr Reye'),(2,'Producción','2/12/2020','08:00:00','Cama 1 ','MP-001',21,198.5,55,'Jefe de Area'),(3,'Producción','3/12/2020','08:00:00','Cama 1','MP-001',22,184.5,69,'Jefe de Area'),(4,'Producción','4/12/2020','08:15:00','Cama 1','MP-001',22,249.5,67,'Jefe de Area'),(5,'Producción','5/12/2020','08:30:00','Cama 1','MP-001',22,246,68,'Jefe de Area'),(6,'Producción','6/12/2020','08:35:00','Cama 1 ','MP-001',20,191,69,'Jefe de Area'),(7,'Producción','7/12/2020','08:00:00','Cama 1 ','MP-001',22,245.5,57,'Jefe de Area'),(8,'Producción','8/12/2020','08:00:00','Cama 2 ','MP-001',21,202.5,57,'Jefe de Area'),(9,'Producción','8/12/2020','09:00:00','Cama 1','MP-002',21,216,58,'Jefe de Area'),(10,'Producción','9/12/2020','08:00:00','Cama 2','MP-001',21,218.5,56,'Jefe de Area'),(11,'Producción','9/12/2020','08:15:00','Cama 1','MP-002',21,206,59,'Jefe de Area'),(12,'Producción','10/12/2020','08:00:00','Cama 2','MP-001',21,196.5,63,'Jefe de Area'),(13,'Producción','10/12/2020','08:15:00','Cama 1','MP-002',20,228,64,'Jefe de Area'),(14,'Producción','11/12/2020','08:15:00','Cama 2','MP-001',22,250,53,'Jefe de Area'),(15,'Producción','11/12/2020','08:30:00','Cama 1','MP-002',21,224,60,'Jefe de Area'),(16,'Producción','12/12/2020','08:30:00','Cama 2','MP-001',22,194.5,59,'Jefe de Area'),(17,'Producción','12/12/2020','08:35:00','Cama 1','MP-002',22,233.5,55,'Jefe de Area'),(18,'Producción','13/12/2020','08:35:00','Cama 2','MP-001',22,234.5,67,'Jefe de Area'),(19,'Producción','13/12/2020','08:45:00','Cama 1','MP-002',22,224.5,56,'Jefe de Area'),(20,'Producción','14/12/2020','08:00:00','Cama 2','MP-001',21,248.5,63,'Jefe de Area'),(21,'Producción','14/12/2020','08:15:00','Cama 1','MP-002',22,181.5,55,'Jefe de Area'),(22,'Producción','15/12/2020','08:00:00','Cama 1','MP-003',22,184,59,'Jefe de Area'),(23,'Producción','15/12/2020','08:10:00','Cama 2','MP-002',21,214,51,'Jefe de Area'),(24,'Producción','15/12/2020','08:20:00','Cama 3 ','MP-001',20,209,70,'Jefe de Area'),(25,'Producción','16/12/2020','08:30:00','Cama 1','MP-003',22,232,65,'Jefe de Area'),(26,'Producción','16/12/2020','08:40:00','Cama 2','MP-002',21,229.5,70,'Jefe de Area'),(27,'Producción','16/12/2020','08:50:00','Cama 3 ','MP-001',21,202,59,'Jefe de Area'),(28,'Producción','17/12/2020','08:30:00','Cama 1','MP-003',20,252,64,'Jefe de Area'),(29,'Producción','17/12/2020','08:40:00','Cama 2','MP-002',22,232,57,'Jefe de Area'),(30,'Producción','17/12/2020','08:50:00','Cama 3 ','MP-001',20,186.5,51,'Jefe de Area'),(31,'Producción','18/12/2020','08:30:00','Cama 1','MP-003',20,245,60,'Jefe de Area'),(32,'Producción','18/12/2020','08:40:00','Cama 2','MP-002',22,239,62,'Jefe de Area'),(33,'Producción','18/12/2020','08:50:00','Cama 3 ','MP-001',20,189.5,58,'Jefe de Area'),(34,'Producción','19/12/2020','08:30:00','Cama 1','MP-003',22,250.5,61,'Jefe de Area'),(35,'Producción','19/12/2020','08:40:00','Cama 2','MP-002',20,227.5,63,'Jefe de Area'),(36,'Producción','19/12/2020','08:50:00','Cama 3 ','MP-001',22,179.5,51,'Jefe de Area'),(37,'Producción','20/12/2020','08:30:00','Cama 1','MP-003',20,241,51,'Jefe de Area'),(38,'Producción','20/12/2020','08:40:00','Cama 2','MP-002',21,224,62,'Jefe de Area'),(39,'Producción','20/12/2020','08:50:00','Cama 3 ','MP-001',20,201.5,60,'Jefe de Area'),(40,'Producción','21/12/2020','08:30:00','Cama 1','MP-003',20,231.5,68,'Jefe de Area'),(41,'Producción','21/12/2020','08:40:00','Cama 2','MP-002',21,222.5,50,'Jefe de Area'),(42,'Producción','21/12/2020','08:50:00','Cama 3 ','MP-001',22,247,63,'Jefe de Area'),(43,'Producción','22/12/2020','08:30:00','Cama 1','MP-004',21,224,62,'Jefe de Area'),(44,'Producción','22/12/2020','08:40:00','Cama 2','MP-003',21,218,69,'Jefe de Area'),(45,'Producción','22/12/2020','08:50:00','Cama 3 ','MP-002',20,210.5,69,'Jefe de Area'),(46,'Producción','22/12/2020','09:15:00','Cama 4','MP-001',22,204,55,'Jefe de Area'),(47,'Producción','23/12/2020','08:30:00','Cama 1','MP-004',22,210.5,69,'Jefe de Area'),(48,'Producción','23/12/2020','08:40:00','Cama 2','MP-003',22,209.5,61,'Jefe de Area'),(49,'Producción','23/12/2020','08:50:00','Cama 3 ','MP-002',21,222.5,56,'Jefe de Area'),(50,'Producción','23/12/2020','09:15:00','Cama 4','MP-001',20,192,62,'Jefe de Area'),(51,'Producción','24/12/2020','08:30:00','Cama 1','MP-004',22,205,52,'Jefe de Area'),(52,'Producción','24/12/2020','08:40:00','Cama 2','MP-003',21,197.5,54,'Jefe de Area'),(53,'Producción','24/12/2020','08:50:00','Cama 3 ','MP-002',22,214.5,63,'Jefe de Area'),(54,'Producción','24/12/2020','09:15:00','Cama 4','MP-001',20,190,51,'Jefe de Area'),(55,'Producción','25/12/2020','08:30:00','Cama 1','MP-004',20,194,59,'Jefe de Area'),(56,'Producción','25/12/2020','08:40:00','Cama 2','MP-003',20,186.5,56,'Jefe de Area'),(57,'Producción','25/12/2020','08:50:00','Cama 3 ','MP-002',21,207.5,60,'Jefe de Area'),(58,'Producción','25/12/2020','09:15:00','Cama 4','MP-001',22,222.5,52,'Jefe de Area'),(59,'Producción','26/12/2020','08:30:00','Cama 1','MP-004',20,218.5,54,'Jefe de Area'),(60,'Producción','26/12/2020','08:40:00','Cama 2','MP-003',20,210.5,57,'Jefe de Area'),(61,'Producción','26/12/2020','08:50:00','Cama 3 ','MP-002',20,188.5,68,'Jefe de Area'),(62,'Producción','26/12/2020','09:15:00','Cama 4','MP-001',22,226.5,70,'Jefe de Area'),(63,'Producción','27/12/2020','08:30:00','Cama 1','MP-004',21,190.5,67,'Jefe de Area'),(64,'Producción','27/12/2020','08:40:00','Cama 2','MP-003',22,252.5,65,'Jefe de Area'),(65,'Producción','27/12/2020','08:50:00','Cama 3 ','MP-002',21,246,61,'Jefe de Area'),(66,'Producción','27/12/2020','09:15:00','Cama 4','MP-001',21,232.5,53,'Jefe de Area'),(67,'Producción','28/12/2020','08:30:00','Cama 1','MP-004',22,206.5,51,'Jefe de Area'),(68,'Producción','28/12/2020','08:40:00','Cama 2','MP-003',22,191.5,55,'Jefe de Area'),(69,'Producción','28/12/2020','08:50:00','Cama 3 ','MP-002',22,211.5,60,'Jefe de Area'),(70,'Producción','28/12/2020','09:15:00','Cama 4','MP-001',21,236,55,'Jefe de Area'),(71,'Producción','29/12/2020','08:30:00','Cama 1','MP-005',22,233.5,63,'Jefe de Area'),(72,'Producción','29/12/2020','08:40:00','Cama 2','MP-004',22,191,58,'Jefe de Area'),(73,'Producción','29/12/2020','08:50:00','Cama 3 ','MP-003',22,207,55,'Jefe de Area'),(74,'Producción','29/12/2020','09:15:00','Cama 4','MP-002',22,240,60,'Jefe de Area'),(75,'Producción','29/12/2020','09:30:00','Cama 5','MP-001',20,181,69,'Jefe de Area'),(76,'Producción','30/12/2020','08:30:00','Cama 1','MP-005',22,181.5,50,'Jefe de Area'),(77,'Producción','30/12/2020','08:40:00','Cama 2','MP-004',20,202,58,'Jefe de Area'),(78,'Producción','30/12/2020','08:50:00','Cama 3 ','MP-003',22,230.5,70,'Jefe de Area'),(79,'Producción','30/12/2020','09:15:00','Cama 4','MP-002',21,194.5,50,'Jefe de Area'),(80,'Producción','30/12/2020','09:30:00','Cama 5','MP-001',21,232,62,'Jefe de Area'),(81,'Producción','31/12/2020','08:30:00','Cama 1','MP-005',20,182,68,'Jefe de Area'),(82,'Producción','31/12/2020','08:40:00','Cama 2','MP-004',21,234,62,'Jefe de Area'),(83,'Producción','31/12/2020','08:50:00','Cama 3 ','MP-003',20,179.5,65,'Jefe de Area'),(84,'Producción','31/12/2020','09:15:00','Cama 4','MP-002',21,198.5,63,'Jefe de Area'),(85,'Producción','31/12/2020','09:30:00','Cama 5','MP-001',22,199,60,'Jefe de Area'),(86,'Producción','1/01/2021','08:30:00','Cama 1','MP-005',21,178.5,63,'Jefe de Area'),(87,'Producción','1/01/2021','08:40:00','Cama 2','MP-004',21,197.5,53,'Jefe de Area'),(88,'Producción','1/01/2021','08:50:00','Cama 3 ','MP-003',20,240.5,54,'Jefe de Area'),(89,'Producción','1/01/2021','09:15:00','Cama 4','MP-002',21,178,51,'Jefe de Area'),(90,'Producción','1/01/2021','09:30:00','Cama 5','MP-001',20,202.5,53,'Jefe de Area'),(91,'Producción','2/01/2021','08:30:00','Cama 1','MP-005',20,184.5,59,'Jefe de Area'),(92,'Producción','2/01/2021','08:40:00','Cama 2','MP-004',21,189,65,'Jefe de Area'),(93,'Producción','2/01/2021','08:50:00','Cama 3 ','MP-003',21,209,50,'Jefe de Area'),(94,'Producción','2/01/2021','09:15:00','Cama 4','MP-002',20,251,56,'Jefe de Area'),(95,'Producción','2/01/2021','09:30:00','Cama 5','MP-001',20,182.5,53,'Jefe de Area'),(96,'Producción','3/01/2021','08:30:00','Cama 1','MP-005',22,175,62,'Jefe de Area'),(97,'Producción','3/01/2021','08:40:00','Cama 2','MP-004',21,193.5,67,'Jefe de Area'),(98,'Producción','3/01/2021','08:50:00','Cama 3 ','MP-003',22,177.5,57,'Jefe de Area'),(99,'Producción','3/01/2021','09:15:00','Cama 4','MP-002',20,228,66,'Jefe de Area'),(100,'Producción','3/01/2021','09:30:00','Cama 5','MP-001',22,211,65,'Jefe de Area'),(101,'Producción','4/01/2021','08:30:00','Cama 1','MP-005',21,180.5,66,'Jefe de Area'),(102,'Producción','4/01/2021','08:40:00','Cama 2','MP-004',21,211.5,61,'Jefe de Area'),(103,'Producción','4/01/2021','08:50:00','Cama 3 ','MP-003',21,196.5,53,'Jefe de Area'),(104,'Producción','4/01/2021','09:15:00','Cama 4','MP-002',20,186,61,'Jefe de Area'),(105,'Producción','4/01/2021','09:30:00','Cama 5','MP-001',21,207,69,'Jefe de Area'),(106,'Producción','5/01/2021','08:30:00','Cama 1','MP-005',20,191,55,'Jefe de Area'),(107,'Producción','5/01/2021','08:40:00','Cama 2','MP-004',22,245.5,64,'Jefe de Area'),(108,'Producción','5/01/2021','08:50:00','Cama 3 ','MP-003',21,181,53,'Jefe de Area'),(109,'Producción','5/01/2021','09:15:00','Cama 4','MP-002',22,214.5,57,'Jefe de Area'),(110,'Producción','5/01/2021','09:30:00','Cama 5','MP-001',20,226.5,69,'Jefe de Area');
/*!40000 ALTER TABLE `producto_en_proceso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto_final`
--

DROP TABLE IF EXISTS `producto_final`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto_final` (
  `ID` varchar(45) NOT NULL,
  `AREA` varchar(45) NOT NULL,
  `FECHA` varchar(45) NOT NULL,
  `HORA_ENTRADA` time NOT NULL,
  `LOTE` varchar(45) NOT NULL,
  `PESO` float NOT NULL,
  `ENCARGADO` varchar(45) NOT NULL,
  `SOPORTE` varchar(45) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto_final`
--

LOCK TABLES `producto_final` WRITE;
/*!40000 ALTER TABLE `producto_final` DISABLE KEYS */;
INSERT INTO `producto_final` VALUES ('0001','Almacen_PF','26/01/2020','11:00:00','MP-001',25,'Supervisor de Planta','Operario 1, Operario 2, Operario 3'),('0002','Almacen_PF','26/01/2020','13:00:00','MP-001',25,'Supervisor de Planta','Operario 1, Operario 2, Operario 3'),('0003','Almacen_PF','26/01/2020','13:00:00','MP-001',25,'Supervisor de Planta','Operario 1, Operario 2, Operario 3');
/*!40000 ALTER TABLE `producto_final` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedores`
--

DROP TABLE IF EXISTS `proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedores` (
  `ID_PROVEDOR` varchar(45) NOT NULL,
  `NOMBRE` varchar(45) NOT NULL,
  `APELLIDO` varchar(45) NOT NULL,
  `EMPRESA` varchar(45) NOT NULL,
  `RUC` varchar(45) NOT NULL,
  `TELEFONO` int NOT NULL,
  `CORREO` varchar(45) NOT NULL,
  `DESCRIPCION` longtext NOT NULL,
  PRIMARY KEY (`ID_PROVEDOR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedores`
--

LOCK TABLES `proveedores` WRITE;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
INSERT INTO `proveedores` VALUES ('PROV-001','Juan ','Rodriguez','Quimica Calltor S.A.C.','20551134912',977635091,'juan.rodriguez@quimica.c@gmail.com','Empresa de microorganismos activadores');
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `FNAME` varchar(45) NOT NULL,
  `LNAME` varchar(45) NOT NULL,
  `CONTACT` varchar(45) NOT NULL,
  `CORREO` varchar(45) NOT NULL,
  `P_SEGURIDAD` varchar(45) NOT NULL,
  `R_SEGURIDAD` varchar(45) NOT NULL,
  `PASSWORD` varchar(45) NOT NULL,
  PRIMARY KEY (`CORREO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES ('Andres','Max','950760999','max@gmail.com','Lugar de nacimiento','Lima','123');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-13 10:03:38
