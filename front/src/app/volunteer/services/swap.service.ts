import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject, throwError } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { AuthService } from 'src/app/auth';
import { environment } from 'src/environments/environment';
import { Swap, SwapPOST } from 'src/app/shared/models/swap';
import { Size } from 'src/app/shared/models/swap';
import { Beneficiary, Child } from 'src/app/shared/models/beneficiary';

@Injectable({
  providedIn: 'root'
})
export class SwapService {

  private baseURL: string;
  _refreshPage$ = new Subject<void>();

  constructor(private http: HttpClient, private authService: AuthService) {
    this.baseURL = environment.baseURL;
  }

  get refreshPage$() {
    return this._refreshPage$;
  }

 /**
   * @description Faz um POST para salvar uma troca
   * @param swap O objeto contendo os dados da troca
   * @returns Um Observable contendo os dados de sucesso ou falha
   */



  // Cria uma nova troca
  createSwap(swap: SwapPOST): Observable<any> {
    return this.http.post(`${this.baseURL}swaps`, swap, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => throwError(() => new Error(`Erro ao criar troca: ${error.message}`)))
      );
  }

 // Lista todas as trocas


listSwaps(): Observable<any> {
  // Correto uso de template literals para inserir a variável
  return this.http.get(`${this.baseURL}swaps`, { headers: this.authService.getHeaders() })
    .pipe(
      catchError(error => throwError(() => new Error(`Erro ao listar trocas: ${error.message}`)))
    );
}


  // Busca uma troca específica pelo ID
  findSwap(id: number): Observable<any> {
    return this.http.get(`${this.baseURL}${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => throwError(() => new Error(`Erro ao encontrar troca: ${error.message}`)))
      );
  }


   /**
   * @description Envia uma requisição PATCH para editar uma campanha existente.
   * @param id Identificador da campanha.
   * @param swap Dados atualizados da campanha.
   * @returns Um Observable contendo os dados de resposta ou erro.
   */
  // Edita uma troca existente
  editSwap(id: number, swap: SwapPOST): Observable<any> {
    return this.http.put(`${this.baseURL}swaps/${id}`, swap, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => throwError(() => new Error(`Erro ao editar troca: ${error.message}`)))
      );
  }


  // Deleta uma troca existente
  deleteSwap(id: number): Observable<any> {
    return this.http.delete(`${this.baseURL}swaps/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => throwError(() => new Error(`Erro ao deletar troca: ${error.message}`)))
      );
  }

  // Lista tamanhos de roupas e sapatos
  listSizes(): Observable<any> {
    return this.http.get(`${this.baseURL}sizes`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  // Lista beneficiários
  listBeneficiaries(): Observable<Beneficiary[]> {
    return this.http.get<Beneficiary[]>(`${this.baseURL}beneficiaries`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => throwError(() => new Error(`Erro ao listar beneficiários: ${error.message}`)))
      );
  }

  // Lista crianças associadas a uma troca
  listChildrenByBenefitedId(benefitedId: number): Observable<Child[]> {
    return this.http.get<Child[]>(`${this.baseURL}/children?benefited_id=${benefitedId}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          throw new Error(`Erro ao buscar crianças por beneficiada: ${error.message}`);
        })
      );
  }
}
