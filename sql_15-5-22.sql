/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - baby_vaccination
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`baby_vaccination` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `baby_vaccination`;

/*Table structure for table `baby` */

DROP TABLE IF EXISTS `baby`;

CREATE TABLE `baby` (
  `baby_id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) DEFAULT NULL,
  `baby_name` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `weight` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`baby_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `baby` */

insert  into `baby`(`baby_id`,`parent_id`,`baby_name`,`dob`,`gender`,`weight`) values (1,2,'tae','5 months','Male','5kg'),(2,2,'kiwii','7 months','Female','10kg');

/*Table structure for table `center` */

DROP TABLE IF EXISTS `center`;

CREATE TABLE `center` (
  `center_id` int(11) DEFAULT NULL,
  `center_name` varchar(100) DEFAULT NULL,
  `center_place` varchar(100) DEFAULT NULL,
  `center_pincode` int(11) DEFAULT NULL,
  `phone_no` varchar(11) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `center` */

insert  into `center`(`center_id`,`center_name`,`center_place`,`center_pincode`,`phone_no`,`email`) values (4,'baby center','by',678889,'9876543234','baby@gmail.com'),(5,'child center','cld',6788990,'9867986756','child@gmail.com');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `u_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`u_type`) values (1,'admin','admin','admin'),(2,'namjoon@gmail.com','1','parent'),(3,'jin@gmail.com','1','parent'),(4,'baby@gmail.com','1','center'),(5,'child@gmail.com','2022','center'),(6,'a@gmail.com','8194','center'),(7,'suga@gmail.com','1','parent');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL,
  `notification` varchar(500) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`notification`,`date`) values (0,'alertttt','2022-05-12');

/*Table structure for table `parent` */

DROP TABLE IF EXISTS `parent`;

CREATE TABLE `parent` (
  `parent_id` int(11) DEFAULT NULL,
  `parent_name` varchar(100) DEFAULT NULL,
  `house_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pincode` int(11) DEFAULT NULL,
  `mob_no` varchar(11) DEFAULT NULL,
  `email_id` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `parent` */

insert  into `parent`(`parent_id`,`parent_name`,`house_name`,`place`,`post`,`pincode`,`mob_no`,`email_id`) values (2,'namjoon','aaaa','bbb','as',343433,'9876543210','namjoon@gmail.com'),(3,'jin','asd','er','gg',454445,'2332113444','jin@gmail.com'),(7,'suga','asw','aaf','nnn',876665,'9879879879','suga@gmail.com');

/*Table structure for table `report` */

DROP TABLE IF EXISTS `report`;

CREATE TABLE `report` (
  `report_id` int(11) NOT NULL AUTO_INCREMENT,
  `vaccine_id` int(11) DEFAULT NULL,
  `baby_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `report` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`report_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `report` */

insert  into `report`(`report_id`,`vaccine_id`,`baby_id`,`date`,`report`) values (1,1,1,'2022-05-12','/static/pic/220512-231259.jpg'),(2,1,2,'2022-05-13','/static/pic/220513-003655.jpg');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `baby_id` int(11) DEFAULT NULL,
  `vaccine_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`request_id`,`baby_id`,`vaccine_id`,`date`,`status`) values (1,1,1,'2022-05-12','approved'),(2,2,3,'2022-05-12','approved'),(3,1,1,'2022-05-13','pending');

/*Table structure for table `vaccine` */

DROP TABLE IF EXISTS `vaccine`;

CREATE TABLE `vaccine` (
  `vaccine_id` int(11) NOT NULL AUTO_INCREMENT,
  `vaccine_name` varchar(100) DEFAULT NULL,
  `center_id` int(11) DEFAULT NULL,
  `slot` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `age_group` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`vaccine_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `vaccine` */

insert  into `vaccine`(`vaccine_id`,`vaccine_name`,`center_id`,`slot`,`date`,`age_group`) values (1,'co vaccine',4,'10','2022-05-13','5-6 months'),(2,'aa vaccine',4,'20','2022-05-25','1-4 months'),(3,'bb bvaccine',4,'15','2022-05-06','6-10 months');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
