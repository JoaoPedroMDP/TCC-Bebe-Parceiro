export class Swap {
    id?: number;                 // Identificador único para a troca
    beneficiaryName: string;    // Nome da pessoa beneficiada pela troca
    clothingSize: string;       // Tamanho da peça de roupa
    shoeSize: string;           // Tamanho do sapato
    status?: string;            // Status da troca (pendente, concluída, etc.)
    createdAt?: Date;           // Data de criação da troca
    updatedAt?: Date;           // Data da última atualização da troca

    constructor(
        beneficiaryName: string,
        clothingSize: string,
        shoeSize: string,
        status?: string,
        id?: number,
        createdAt?: Date,
        updatedAt?: Date
    ) {
        this.id = id;
        this.beneficiaryName = beneficiaryName;
        this.clothingSize = clothingSize;
        this.shoeSize = shoeSize;
        this.status = status;
        this.createdAt = createdAt;
        this.updatedAt = updatedAt;
    }
}
