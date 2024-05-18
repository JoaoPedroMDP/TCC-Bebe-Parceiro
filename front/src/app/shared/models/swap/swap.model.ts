
import { Beneficiary, Child } from "../beneficiary";
import { Status } from "./status.model";
import { Size } from "./size.model";

export class Swap {
  constructor(
    public id?: number,
    public cloth_size?: Size,
    public shoe_size?: Size,
    public description?: string,
    public status?: Status,
    public beneficiary?: Beneficiary,
    public child?: Child
  ) { }
}

// Para representar o modelo de POST, onde apenas os IDs são enviados
export class SwapPOST {
  constructor(
    public id?: number,
    public cloth_size_id?: number,
    public shoe_size_id?: number,
    public description?: string,
    public status_id?: number,
    public beneficiary_id?: number,
    public child_id?: number
  ) { }

  transformObjectToEdit(swap: Swap) {
    this.id = swap.id;
    this.cloth_size_id = swap.cloth_size?.id;
    this.shoe_size_id = swap.shoe_size?.id;
    this.description = swap.description;
    this.status_id = swap.status?.id;
    this.beneficiary_id = swap.beneficiary?.id;
    this.child_id = swap.child?.id
  }
}
