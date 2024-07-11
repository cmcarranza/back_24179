CREATE DATABASE IF NOT EXISTS api_videos;

USE api_videos;

CREATE TABLE IF NOT EXISTS `videos` (
  `id_video` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) NOT NULL,
  `genero` varchar(100) NOT NULL,
  `grupo` varchar(100) NOT NULL,
  `anio` date NOT NULL,
  PRIMARY KEY (`id_video`)
);
