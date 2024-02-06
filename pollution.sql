-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Station`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Station` (
  `SiteID` INT NOT NULL,
  `geo_point_2d` VARCHAR(45) NULL,
  `Location` VARCHAR(45) NULL,
  PRIMARY KEY (`SiteID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Reading`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Reading` (
  `readingId` INT NOT NULL,
  `Date_Time` DATE NULL,
  `NOX` FLOAT NULL,
  `NO2` FLOAT NULL,
  `NO` FLOAT NULL,
  `NVPM10` FLOAT NULL,
  `VPM10` FLOAT NULL,
  `NVPM25` FLOAT NULL,
  `CO` FLOAT NULL,
  `SO2` FLOAT NULL,
  `O3` FLOAT NULL,
  `PM10` FLOAT NULL,
  `PM25` FLOAT NULL,
  `VPM25` FLOAT NULL,
  `Temperature` FLOAT NULL,
  `RH` FLOAT NULL,
  `Air_Pressure` FLOAT NULL,
  `Current` TINYINT NULL,
  `DateStart` DATE NULL,
  `Instrument_Type` VARCHAR(45) NULL,
  `Station_SiteID` INT NOT NULL,
  PRIMARY KEY (`readingId`, `Station_SiteID`),
  INDEX `fk_Reading_Station_idx` (`Station_SiteID` ASC) VISIBLE,
  CONSTRAINT `fk_Reading_Station`
    FOREIGN KEY (`Station_SiteID`)
    REFERENCES `mydb`.`Station` (`SiteID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`MeasureSchema`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`MeasureSchema` (
  `Measure` INT NOT NULL,
  `Description` VARCHAR(45) NULL,
  `unit` VARCHAR(45) NULL,
  PRIMARY KEY (`Measure`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
