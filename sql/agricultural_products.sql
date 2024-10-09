/*
 Navicat Premium Data Transfer

 Source Server         : YMT
 Source Server Type    : MySQL
 Source Server Version : 50743 (5.7.43-log)
 Source Host           : 123.249.36.184:3306
 Source Schema         : agricultural_products

 Target Server Type    : MySQL
 Target Server Version : 50743 (5.7.43-log)
 File Encoding         : 65001

 Date: 09/10/2024 10:42:11
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for ymt_products
-- ----------------------------
DROP TABLE IF EXISTS `ymt_products`;
CREATE TABLE `ymt_products`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `area` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '地区',
  `category` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '产品类型',
  `price` decimal(10, 2) NULL DEFAULT NULL COMMENT '价格（元/斤）',
  `change` decimal(10, 2) NULL DEFAULT NULL COMMENT '涨跌（元/斤）',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_area`(`area`) USING BTREE,
  INDEX `idx_category`(`category`) USING BTREE,
  INDEX `idx_price`(`price`) USING BTREE,
  INDEX `idx_area_category`(`area`, `category`) USING BTREE,
  INDEX `idx_price_change`(`price`, `change`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of ymt_products
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
