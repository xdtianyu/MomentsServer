-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2015-11-01 19:32:28
-- 服务器版本： 5.5.44-MariaDB-1ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `moments`
--

-- --------------------------------------------------------

--
-- 表的结构 `comment`
--

CREATE TABLE `comment` (
  `id` int(11) NOT NULL,
  `sender` int(11) NOT NULL,
  `content` text COLLATE utf8_unicode_ci,
  `time_post` int(11) NOT NULL,
  `time_update` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `comment`
--

INSERT INTO `comment` (`id`, `sender`, `content`, `time_post`, `time_update`) VALUES
(1, 1, 'great', 1446353495, 1446355439),
(2, 1, '哈哈哈', 1446352495, 1446355439),
(4, 2, '哈哈哈', 1446376373, 1446376373),
(5, 2, '哈哈哈哦哦哦', 1446376430, 1446376430);

-- --------------------------------------------------------

--
-- 表的结构 `image`
--

CREATE TABLE `image` (
  `id` int(11) NOT NULL,
  `url` text COLLATE utf8_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `image`
--

INSERT INTO `image` (`id`, `url`) VALUES
(1, 'http://theakiba.com/images/2013/03/4048_moepic1.png'),
(2, 'http://i.imgur.com/DWs03lR.jpg'),
(3, 'http://theakiba.com/images/2013/03/4048_moepic7.jpg'),
(6, 'https://openranka.files.wordpress.com/2013/06/31447949.jpg'),
(7, 'http://img1.ak.crunchyroll.com/i/spire3/80e01e22da63d0a4a12791206a6784d21424538006_full.jpg'),
(8, 'https://openranka.files.wordpress.com/2013/06/31447949.jpg'),
(9, 'http://img1.ak.crunchyroll.com/i/spire3/80e01e22da63d0a4a12791206a6784d21424538006_full.jpg');

-- --------------------------------------------------------

--
-- 表的结构 `tweet`
--

CREATE TABLE `tweet` (
  `id` int(11) NOT NULL,
  `sender` int(11) NOT NULL,
  `content` text COLLATE utf8_unicode_ci,
  `images` text COLLATE utf8_unicode_ci,
  `comments` text COLLATE utf8_unicode_ci,
  `time_post` int(11) NOT NULL,
  `time_update` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `tweet`
--

INSERT INTO `tweet` (`id`, `sender`, `content`, `images`, `comments`, `time_post`, `time_update`) VALUES
(1, 2, '测试', NULL, NULL, 1446351495, 1446351495),
(2, 1, 'testhahah哈哈哈', '1,2', NULL, 1446352495, 1446352495),
(3, 2, '哈哈哈哈啊第三大三', '3', '1,2', 1446353395, 1446353395),
(4, 2, '的萨打算dadasdasda发萨福', '1,2,3', NULL, 1446353495, 1446353495),
(5, 1, 'test', NULL, NULL, 1446362639, 1446362639),
(6, 1, '测试', NULL, NULL, 1446363118, 1446363118),
(7, 1, '测试嗖嗖嗖嗖', '6,7', NULL, 1446363839, 1446363839),
(8, 1, '测试嗖嗖啊的萨的萨阿斯顿萨', '8,9', '4,5', 1446363876, 1446363876);

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `password` text COLLATE utf8_unicode_ci NOT NULL,
  `nick` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `avatar` varchar(256) COLLATE utf8_unicode_ci DEFAULT NULL,
  `profile_image` varchar(256) COLLATE utf8_unicode_ci DEFAULT NULL,
  `friends` text COLLATE utf8_unicode_ci NOT NULL,
  `time_register` int(11) NOT NULL,
  `time_last_login` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password`, `nick`, `avatar`, `profile_image`, `friends`, `time_register`, `time_last_login`) VALUES
(1, 'tianyu', 'tianyu@xdty.org', '123456', 'tianyu', 'https://33.media.tumblr.com/avatar_85177c2ee2c6_128.png', 'http://theakiba.com/images/2013/03/4048_moepic1.png', '2', 1446351495, 1446351495),
(2, 'jsmith', 'jsmith@xdty.org', '123456', 'John Smith', 'http://info.thoughtworks.com/rs/thoughtworks2/images/glyph_badge.png', 'http://img2.findthebest.com/sites/default/files/688/media/images/Mingle_159902_i0.png', '1', 1446352495, 1446352495);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comment`
--
ALTER TABLE `comment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `image`
--
ALTER TABLE `image`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tweet`
--
ALTER TABLE `tweet`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `comment`
--
ALTER TABLE `comment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- 使用表AUTO_INCREMENT `image`
--
ALTER TABLE `image`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- 使用表AUTO_INCREMENT `tweet`
--
ALTER TABLE `tweet`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- 使用表AUTO_INCREMENT `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
