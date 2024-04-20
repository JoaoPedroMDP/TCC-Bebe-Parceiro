import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject, catchError, tap, throwError } from 'rxjs';
import { AuthService } from 'src/app/auth';
import { Professional, ProfessionalPost } from 'src/app/shared/models/professional';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ProfessionalService {

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
   * @description Faz um POST para salvar um profissional
   * @param professional O objeto contendo os dados do profissional
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  createProfessional(professional: ProfessionalPost): Observable<any> {
    return this.http.post(`${this.baseURL}professionals`, professional)
      .pipe(
        tap(() => this.refreshPage$.next()), // Após a execução, emite um evento para os assinantes.
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um DELETE para obter excluir um profissional
   * @param id o Id da especialidade a ser excluída
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  deleteProfessional(id: number): Observable<any> {
    return this.http.delete(`${this.baseURL}professionals/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this.refreshPage$.next()), // Após a execução, emite um evento para os assinantes.
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um PATCH para editar um professional
   * @param id ID do professional necessário para a rota de patch
   * @param professional valor a ser atualizado no body da requisição
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  editProfessional(id: number, professional: Professional): Observable<any> {
    return this.http.patch(`${this.baseURL}professionals/${id}`, professional, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this.refreshPage$.next()), // Após a execução, emite um evento para os assinantes.
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um GET para pegar os dados de um profissional especifico
   * @param id id do professional
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  findProfessional(id: number): Observable<any> {
    return this.http.get(`${this.baseURL}specialities/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um GET para obter todos os profissionais cadastradas
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  listProfessionals(): Observable<any> {
    return this.http.get(`${this.baseURL}professionals`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }
}
