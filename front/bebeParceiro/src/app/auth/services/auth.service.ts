import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor() { }

  validarCodigo(codigo: string): Observable<any> {
    // alterar pela logica de negócio no futuro
    let ex!: Observable<any>;
    return ex;
  }
}
