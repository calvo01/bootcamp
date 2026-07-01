CREATE TABLE usuarios (
    id INT,
    nome VARCHAR(255) NOT NULL COMMENT 'nome do usuario',
    email VARCHAR(100) NOT NULL UNIQUE COMMENT 'email do user',
    endereco VARCHAR(50) NOT NULL COMMENT 'endereco do user',
    data_nascimento DATE NOT NULL COMMENT 'data de nascimento do user'
);

CREATE TABLE viagens.destinos (
    id INT,
    nome VARCHAR(255) NOT NULL UNIQUE COMMENT 'NOME DO DESTINO',
    descricao VARCHAR(255) NOT NULL COMMENT 'DESCRIÇÃO DO LOCAL'
);

CREATE TABLE viagens.reservas (
    id INT,
    id_user INT,
    id_destino INT,
    data_viagem DATE,
    status VARCHAR(255) DEFAULT 'confirmada'
);

CREATE TABLE pagamentos (
    id INT NOT NULL COMMENT 'ID PAGAMENTO',
    id_reserva INT NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    data_pagamento DATE NOT NULL,
    metodo_pagamento VARCHAR(50) NOT NULL COMMENT 'cartao, pix, boleto',
    status_pagamento VARCHAR(50) DEFAULT 'pendente' COMMENT 'pendente, aprovado, recusado'
);