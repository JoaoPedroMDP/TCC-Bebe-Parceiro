import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject, catchError, tap, throwError } from 'rxjs';
import { AuthService } from 'src/app/auth';
import { Benefited } from 'src/app/shared';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class VolunteerService {

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
   * @description Faz um POST para criar códigos de acesso
   * @param amount Quantidade de códigos a serem gerados
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  createAccessCodes(amount: number): Observable<any> {
    let body: { amount: number } = { amount } // Não pode só enviar um int, tem que ser um objeto
    return this.http.post(`${this.baseURL}access_codes`, body, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um POST para inserir os dados de beneficiada
   * @param benefited O objeto beneficiada para ser enviado no body da requisição
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  createBenefited(benefited: Benefited): Observable<any> {
    return this.http.post(`${this.baseURL}beneficiaries/create`, benefited, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um DELETE para obter excluir uma beneficiada
   * @param id o Id da beneficiada a ser excluída
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  deleteBenefited(id: number): Observable<any> {
    return this.http.delete(`${this.baseURL}beneficiaries/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this.refreshPage$.next()), // Após a execução bem-sucedida, emite um evento para os assinantes.
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um PATCH para obter editar uma beneficiada
   * @param id ID da beneficiada necessário para a rota de patch
   * @param benefited valor a ser atualizado no body da requisição
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  editBenefited(id: number, benefited: Benefited): Observable<any> {
    return this.http.patch(`${this.baseURL}beneficiaries/${id}`, benefited, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um GET para obter dados de uma especifica beneficiada
   * @param id da beneficiada
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  findBenefited(id: number): Observable<any> {
    return this.http.get(`${this.baseURL}beneficiaries/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um GET para pegar os dados do Estado Civil  
   * @param id id do Estado Civil
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  findCity(id: number): Observable<any> {
    return this.http.get(`${this.baseURL}cities/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um GET para pegar os dados do Estado Civil  
   * @param id id do Estado Civil
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  findMaritalStatus(id: number): Observable<any> {
    return this.http.get(`${this.baseURL}marital_statuses/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um GET para obter todos os códigos de acesso que não foram usados
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  listAccessCodes(): Observable<any> {
    return this.http.get(`${this.baseURL}access_codes?used=false`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um GET para obter todas as beneficiadas cadastradas
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  listBenefited(): Observable<any> {
    return this.http.get(`${this.baseURL}beneficiaries`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }
}
