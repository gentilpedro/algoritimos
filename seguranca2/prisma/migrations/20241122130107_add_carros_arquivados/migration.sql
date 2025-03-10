-- CreateTable
CREATE TABLE `carrosArquivados` (
    `id` INTEGER NOT NULL,
    `modelo` VARCHAR(30) NOT NULL,
    `marca` VARCHAR(20) NOT NULL,
    `cor` VARCHAR(30) NULL,
    `ano` SMALLINT NOT NULL,
    `preco` DECIMAL(10, 2) NOT NULL,
    `combustivel` ENUM('FLEX', 'GASOLINA', 'ALCOOL', 'DIESEL', 'ELETRICIDADE') NOT NULL DEFAULT 'FLEX',
    `km` MEDIUMINT NOT NULL DEFAULT 0,
    `usuarioId` INTEGER NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `carrosArquivados` ADD CONSTRAINT `carrosArquivados_usuarioId_fkey` FOREIGN KEY (`usuarioId`) REFERENCES `usuarios`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;
