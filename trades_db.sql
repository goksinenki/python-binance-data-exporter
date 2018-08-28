SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `trades2`
-- ----------------------------
DROP TABLE IF EXISTS `trades2`;
CREATE TABLE `trades2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(25) CHARACTER SET utf8 NOT NULL,
  `coinname` text CHARACTER SET utf8 NOT NULL,
  `24hr` double NOT NULL,
  `price` double(15,10) NOT NULL,
  `volume` double NOT NULL,
  `dipfiyat` double(15,10) NOT NULL,
  `tavanfiyat` double(15,10) NOT NULL,
  `yuzdefark` double NOT NULL,
  `buybtctoplam` double NOT NULL,
  `sellbtctoplam` double NOT NULL,
  `tbtcbuytoplam` double NOT NULL,
  `tbtcselltoplam` double NOT NULL,
  `tradebtcyuzdefark` double NOT NULL,
  `candlevolume` double NOT NULL,
  `candleopen` double(15,10) NOT NULL,
  `candleclose` double(15,10) NOT NULL,
  `buyprice0` double(15,10) NOT NULL,
  `buyvolume0` double NOT NULL,
  `sellprice0` double(15,10) NOT NULL,
  `sellvolume0` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of trades2
-- ----------------------------
