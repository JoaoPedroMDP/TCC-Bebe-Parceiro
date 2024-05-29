import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject, catchError, tap, throwError } from 'rxjs';
import { AuthService } from 'src/app/auth';
import { Beneficiary } from 'src/app/shared';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class EvaluationServiceService {

  private baseURL!: string;
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
   * @description Faz um GET para obter todas as beneficiadas cadastradas que estão pendentes
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  listPendingBeneficiaries(): Observable<any> {
    return this.http.get(`${this.baseURL}beneficiaries/pending`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um PATCH para approvar uma beneficiada
   * @param id ID da beneficiada
   * @param datetime Data da admissão
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  approveBeneficiary(id: number, datetime: Date): Observable<any> {
    // Cria o objeto com as chaves específicas
    let body = {
      datetime: datetime,
      volunteer_id: id
    };
    return this.http.patch(`${this.baseURL}beneficiaries/approve/${id}`, body, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this.refreshPage$.next()), // Após a execução, emite um evento para os assinantes.
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }
}
