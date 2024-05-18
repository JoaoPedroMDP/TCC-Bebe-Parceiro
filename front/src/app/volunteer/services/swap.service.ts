import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject, throwError } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { AuthService } from 'src/app/auth';
import { environment } from 'src/environments/environment';
import { SwapPOST, Beneficiary, Child } from 'src/app/shared/models';

@Injectable({
  providedIn: 'root'
})
export class SwapService {

  private baseURL: string = environment.baseURL;
  _refreshPage$ = new Subject<void>();

  constructor(private http: HttpClient, private authService: AuthService) {}

  get refreshPage$() {
    return this._refreshPage$;
  }

  createSwap(swap: SwapPOST): Observable<any> {
    return this.http.post(`${this.baseURL}/swaps`, swap, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => throwError(() => new Error(`Erro ao criar troca: ${error.message}`)))
      );
  }

  listSwaps(): Observable<any> {
    return this.http.get(`${this.baseURL}/swaps`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => throwError(() => new Error(`Erro ao listar trocas: ${error.message}`)))
      );
  }

  getSwap(id: number): Observable<any> {
    return this.http.get(`${this.baseURL}/swaps/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => throwError(() => new Error(`Erro ao encontrar troca: ${error.message}`)))
      );
  }

  editSwap(id: number, swap: SwapPOST): Observable<any> {
    return this.http.patch(`${this.baseURL}/swaps/${id}`, swap, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => throwError(() => new Error(`Erro ao editar troca: ${error.message}`)))
      );
  }

  deleteSwap(id: number): Observable<any> {
    return this.http.delete(`${this.baseURL}/swaps/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => throwError(() => new Error(`Erro ao deletar troca: ${error.message}`)))
      );
  }

  listSizes(): Observable<any> {
    return this.http.get(`${this.baseURL}/sizes`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => throwError(() => new Error(`${error.status} - ${error.error.message}`)))
      );
  }

  listBeneficiaries(): Observable<Beneficiary[]> {
    return this.http.get<Beneficiary[]>(`${this.baseURL}/beneficiaries`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => throwError(() => new Error(`Erro ao listar beneficiários: ${error.message}`)))
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

  listChildrenByBenefitedId(benefitedId: number): Observable<Child[]> {
    return this.http.get<Child[]>(`${this.baseURL}/children?benefited_id=${benefitedId}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => throwError(() => new Error(`Erro ao buscar crianças por beneficiada: ${error.message}`)))
      );
  }

    /**
   * @description Faz um GET para pegar os dados dos filhos da beneficiada
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
    listChildren(): Observable<any> {
      return this.http.get(`${this.baseURL}children?born=true`, { headers: this.authService.getHeaders() })
        .pipe(
          catchError(error => {
            return throwError(() => new Error(`${error.status} - ${error.error.message}`));
          })
        );
    }

    listChildrenByBeneficiaryId(beneficiaryId: number): Observable<Child[]> {
      return this.http.get<Child[]>(`${this.baseURL}/children?beneficiary_id=${beneficiaryId}`, {
          headers: this.authService.getHeaders()
      }).pipe(
          catchError(error => {
              console.error('Erro ao buscar crianças', error);
              return throwError(() => new Error('Erro ao buscar crianças'));
          })
      );
  }
}
