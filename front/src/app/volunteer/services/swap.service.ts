import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject, throwError } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { AuthService } from 'src/app/auth';
import { Child, SwapPOST } from 'src/app/shared/models';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class SwapService {

  private baseURL: string;
  // O Subject irá emitir um valor quando um valor novo for publicado.
  _refreshPage$ = new Subject<void>();

  constructor(private http: HttpClient, private authService: AuthService) {
    this.baseURL = environment.baseURL;
  }

  /**
   * @description Método getter público que expõe _refreshPage$ como um Observable.
   * Isso permite que os componentes se inscrevam no Observable, 
   * mas não podem emitir valores para ele, mantendo o encapsulamento.
   */
  get refreshPage$() {
    return this._refreshPage$;
  }

  /**
   * @description Envia uma requisição POST para criar uma nova troca.
   * @param swap Objeto com os dados da troca para criação.
   * @returns Um Observable contendo os dados de resposta ou erro.
   */
  createSwap(swap: SwapPOST): Observable<any> {
    return this.http.post(`${this.baseURL}/swaps`, swap, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Envia uma requisição DELETE para remover uma troca pelo ID.
   * @param id Identificador da troca a ser deletada.
   * @returns Um Observable contendo os dados de resposta ou erro.
   */
  deleteSwap(id: number): Observable<any> {
    return this.http.delete(`${this.baseURL}/swaps/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Envia uma requisição PATCH para editar uma troca existente.
   * @param id Identificador da troca.
   * @param swap Dados atualizados da troca.
   * @returns Um Observable contendo os dados de resposta ou erro.
   */
  editSwap(id: number, swap: SwapPOST): Observable<any> {
    return this.http.patch(`${this.baseURL}/swaps/${id}`, swap, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um GET para pegar os crianças de uma beneficiada especifica
   * @param beneficiaryId ID da beneficiada
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  listChildrenByBeneficiaryId(beneficiaryId: number): Observable<Child[]> {
    return this.http.get<Child[]>(`${this.baseURL}/children?beneficiary_id=${beneficiaryId}`, {
      headers: this.authService.getHeaders()
    }).pipe(
      catchError(error => {
        return throwError(() => new Error(`${error.status} - ${error.error.message}`));
      })
    );
  }

  /**
   * @description Faz um GET para pegar os dados dos tamanhos de roupa
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  listClothSizes(): Observable<any> {
    return this.http.get(`${this.baseURL}sizes?type=Roupa`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um GET para pegar os dados dos tamanhos de sapatos
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  listShoeSizes(): Observable<any> {
    return this.http.get(`${this.baseURL}sizes?type=Sapato`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Busca todas os status do sistema
   * @returns Um Observable contendo uma lista de campanhas ou erro.
   */
  listStatuses(): Observable<any> {
    return this.http.get(`${this.baseURL}/status`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Busca todas as trocas cadastradas.
   * @returns Um Observable contendo uma lista de campanhas ou erro.
   */
  listSwaps(): Observable<any> {
    return this.http.get(`${this.baseURL}/swaps`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }
}
