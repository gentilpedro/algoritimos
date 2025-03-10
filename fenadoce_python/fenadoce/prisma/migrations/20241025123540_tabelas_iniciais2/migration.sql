/*
  Warnings:

  - You are about to drop the `candidatos` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE `votos` DROP FOREIGN KEY `votos_candidataId_fkey`;

-- DropTable
DROP TABLE `candidatos`;

-- CreateTable
CREATE TABLE `candidatas` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `nome` VARCHAR(30) NOT NULL,
    `clube` VARCHAR(30) NOT NULL,
    `idade` SMALLINT NOT NULL,
    `sonho` VARCHAR(191) NOT NULL,
    `numVotos` INTEGER NOT NULL DEFAULT 0,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `votos` ADD CONSTRAINT `votos_candidataId_fkey` FOREIGN KEY (`candidataId`) REFERENCES `candidatas`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;
