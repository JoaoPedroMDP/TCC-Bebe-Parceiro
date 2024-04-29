import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject, catchError, tap, throwError } from 'rxjs';
import { AuthService } from 'src/app/auth';
import { Speciality } from 'src/app/shared/models/professional';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class SpecialityService {

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
   * @description Faz um POST para inserir os dados de especialidade
   * @param speciality O objeto especialidade para ser enviado no body da requisição
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  createSpeciality(speciality: Speciality): Observable<any> {
    return this.http.post(`${this.baseURL}specialities`, speciality, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this.refreshPage$.next()), // Após a execução, emite um evento para os assinantes.
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um DELETE para obter excluir uma especialidade
   * @param id o Id da especialidade a ser excluída
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  deleteSpeciality(id: number): Observable<any> {
    return this.http.delete(`${this.baseURL}specialities/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this.refreshPage$.next()), // Após a execução, emite um evento para os assinantes.
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um PATCH para editar uma especialidade
   * @param id ID da especialidade necessário para a rota de patch
   * @param speciality valor a ser atualizado no body da requisição
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  editSpeciality(id: number, speciality: Speciality): Observable<any> {
    return this.http.patch(`${this.baseURL}specialities/${id}`, speciality, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this.refreshPage$.next()), // Após a execução, emite um evento para os assinantes.
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um GET para pegar os dados de uma especialidade especifica
   * @param id id da especialidade
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  findSpeciality(id: number): Observable<any> {
    return this.http.get(`${this.baseURL}specialities/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um GET para obter todas as especialidades cadastradas
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  listSpecialities(): Observable<any> {
    return this.http.get(`${this.baseURL}specialities`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }
}
