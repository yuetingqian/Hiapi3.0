-- MySQL dump 10.13  Distrib 5.5.32, for debian-linux-gnu (i686)
--
-- Host: 192.168.201.51    Database: Hiapi3
-- ------------------------------------------------------
-- Server version	5.0.77

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
-- Not dumping tablespaces as no INFORMATION_SCHEMA.FILES table on this server
--

--
-- Table structure for table `apis`
--

DROP TABLE IF EXISTS `apis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `apis` (
  `id` int(10) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL COMMENT 'api名字',
  `cn_name` varchar(100) default '' COMMENT 'api中文名',
  `version` varchar(50) NOT NULL default '' COMMENT 'api版本，如1.3等',
  `pass_ver` varchar(100) default '' COMMENT 'api测试通过版本，如2012_42_02',
  `method` varchar(50) NOT NULL default '' COMMENT '请求方法',
  `wiki_url` varchar(200) default '' COMMENT 'wiki地址',
  `lasttime` varchar(100) default '' COMMENT '最后测试时间',
  `description` varchar(500) default '' COMMENT 'api描述',
  `req_field` varchar(50) default '' COMMENT '当该参数被设置时，才进行请求',
  `tr` varchar(500) default '' COMMENT '用来分行的字段',
  `category` varchar(100) default '' COMMENT 'api分类',
  `req_url` varchar(200) default '' COMMENT '请求url',
  `is_login` int(10) default '0' COMMENT '是否需要登录，1为需要，0为不需要',
  `warning` varchar(100) default '' COMMENT '该值为空时，json返回数据不存在，状态改为warning',
  `is_deleted` int(10) default '0' COMMENT '该值为0表示未删除，为1表示逻辑删除',
  `app_id` int(10) default '0',
  `updated_at` varchar(45) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `index2` (`name`,`app_id`,`version`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apis`
--

LOCK TABLES `apis` WRITE;
/*!40000 ALTER TABLE `apis` DISABLE KEYS */;
/*!40000 ALTER TABLE `apis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `apps`
--

DROP TABLE IF EXISTS `apps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `apps` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(45) NOT NULL,
  `sharekey` varchar(100) default NULL,
  `pubkey` varchar(100) default NULL,
  `sigtype` int(11) NOT NULL COMMENT '1、旧签名 2、新签名',
  `ord` int(11) NOT NULL COMMENT '排序参数，越小越靠前',
  `updated_at` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `index2` (`name`,`sigtype`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='app信息表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apps`
--

LOCK TABLES `apps` WRITE;
/*!40000 ALTER TABLE `apps` DISABLE KEYS */;
INSERT INTO `apps` VALUES (1,'1231','131','321',0,0,'0000-00-00 00:00:00'),(2,'fsaf',NULL,NULL,0,0,'0000-00-00 00:00:00');
/*!40000 ALTER TABLE `apps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auto_param_inputs`
--

DROP TABLE IF EXISTS `auto_param_inputs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auto_param_inputs` (
  `id` int(10) NOT NULL auto_increment,
  `name` varchar(50) default '' COMMENT '参数名',
  `auto_type` int(10) NOT NULL COMMENT '自动化类型',
  `type` int(10) default NULL COMMENT '组合的序号.',
  `value` varchar(100) default '' COMMENT '参数值',
  `api_id` int(10) default NULL COMMENT 'apis表里的id',
  `updated_at` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `index2` (`name`,`api_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auto_param_inputs`
--

LOCK TABLES `auto_param_inputs` WRITE;
/*!40000 ALTER TABLE `auto_param_inputs` DISABLE KEYS */;
/*!40000 ALTER TABLE `auto_param_inputs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auto_param_outputs`
--

DROP TABLE IF EXISTS `auto_param_outputs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auto_param_outputs` (
  `id` int(10) NOT NULL auto_increment,
  `parent` varchar(100) default '' COMMENT '父类',
  `name` varchar(50) default '' COMMENT '参数名',
  `auto_type` int(10) NOT NULL COMMENT '自动化类型',
  `type` int(10) default NULL COMMENT '组合的序号.',
  `value` varchar(1000) default '' COMMENT '参数值',
  `api_id` int(10) default NULL COMMENT 'apis表里的id',
  `updated_at` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `index2` (`parent`,`name`,`api_id`,`auto_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auto_param_outputs`
--

LOCK TABLES `auto_param_outputs` WRITE;
/*!40000 ALTER TABLE `auto_param_outputs` DISABLE KEYS */;
/*!40000 ALTER TABLE `auto_param_outputs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auto_report_details`
--

DROP TABLE IF EXISTS `auto_report_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auto_report_details` (
  `api_id` int(10) NOT NULL COMMENT 'apiid',
  `exec_datetime` datetime default NULL,
  `filename` varchar(100) default NULL,
  `link` varchar(1000) default NULL,
  `result` varchar(100) default NULL,
  `error_code` varchar(10) default '',
  `error_message` varchar(500) default ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auto_report_details`
--

LOCK TABLES `auto_report_details` WRITE;
/*!40000 ALTER TABLE `auto_report_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `auto_report_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auto_reports`
--

DROP TABLE IF EXISTS `auto_reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auto_reports` (
  `app_id` int(10) NOT NULL COMMENT 'appid',
  `exec_datetime` datetime default NULL,
  `filename` varchar(100) default NULL,
  `api_release_version` varchar(100) default NULL,
  `result` varchar(100) default NULL,
  `info` varchar(100) default '',
  `auto_type` int(10) NOT NULL COMMENT '自动化类型'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auto_reports`
--

LOCK TABLES `auto_reports` WRITE;
/*!40000 ALTER TABLE `auto_reports` DISABLE KEYS */;
/*!40000 ALTER TABLE `auto_reports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bs_inputs`
--

DROP TABLE IF EXISTS `bs_inputs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bs_inputs` (
  `app_id` int(10) NOT NULL default '0',
  `param` varchar(50) NOT NULL COMMENT '参数名',
  `value` varchar(100) default NULL COMMENT '参数值',
  `description` varchar(100) default NULL COMMENT '参数中文描述',
  `updated_at` datetime NOT NULL,
  PRIMARY KEY  (`app_id`,`param`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bs_inputs`
--

LOCK TABLES `bs_inputs` WRITE;
/*!40000 ALTER TABLE `bs_inputs` DISABLE KEYS */;
/*!40000 ALTER TABLE `bs_inputs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `param_inputs`
--

DROP TABLE IF EXISTS `param_inputs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `param_inputs` (
  `id` int(32) NOT NULL auto_increment,
  `name` varchar(50) default '' COMMENT '参数英文名',
  `cn_name` varchar(50) default '' COMMENT '参数中文名',
  `type` varchar(20) default '' COMMENT '参数类型',
  `value` varchar(100) default '' COMMENT '参数值',
  `info` varchar(100) default '' COMMENT '备注',
  `is_required` tinyint(1) default '0' COMMENT '是否必填',
  `is_linefeed` int(10) default '1' COMMENT '改api是否独占一行',
  `ord` int(10) default '0' COMMENT '排序，越小越靠前',
  `api_id` int(10) NOT NULL default '0' COMMENT 'apis里的id',
  `updated_at` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `index2` (`name`,`api_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `param_inputs`
--

LOCK TABLES `param_inputs` WRITE;
/*!40000 ALTER TABLE `param_inputs` DISABLE KEYS */;
/*!40000 ALTER TABLE `param_inputs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `param_outputs`
--

DROP TABLE IF EXISTS `param_outputs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `param_outputs` (
  `id` int(11) NOT NULL auto_increment COMMENT '自增id',
  `name` varchar(50) default '' COMMENT '返回字段英文名',
  `cn_name` varchar(100) default '' COMMENT '返回字段中文名',
  `type` varchar(30) default '' COMMENT '返回字段正确的类型',
  `parent` varchar(100) default '' COMMENT '父节点id',
  `api_id` int(10) NOT NULL default '0' COMMENT 'apis里的id',
  `updated_at` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `index2` (`name`,`parent`,`api_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `param_outputs`
--

LOCK TABLES `param_outputs` WRITE;
/*!40000 ALTER TABLE `param_outputs` DISABLE KEYS */;
/*!40000 ALTER TABLE `param_outputs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-10-29  9:18:42
