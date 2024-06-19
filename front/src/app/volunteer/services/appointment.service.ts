import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject, catchError, tap, throwError } from 'rxjs';
import { AuthService } from 'src/app/auth';
import { AppointmentPOST } from 'src/app/shared/models/appointment/appointment.model';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AppointmentService {

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
   * @description Faz um POST para salvar um atendimento
   * @param appointment O objeto contendo os dados do atendimento
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  createAppointment(appointment: AppointmentPOST): Observable<any> {
    return this.http.post(`${this.baseURL}appointments`, appointment, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this.refreshPage$.next()), // Após a execução, emite um evento para os assinantes.
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um DELETE para obter excluir um atendimento
   * @param id O Id do atendimento a ser excluída
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  deleteAppointment(id: number): Observable<any> {
    return this.http.delete(`${this.baseURL}appointments/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this.refreshPage$.next()), // Após a execução, emite um evento para os assinantes.
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um PATCH para editar um atendimento
   * @param id ID do atendimento necessário para a rota de patch
   * @param appointment valor a ser atualizado no body da requisição
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  editAppointment(id: number, appointment: AppointmentPOST): Observable<any> {
    return this.http.patch(`${this.baseURL}appointments/${id}`, appointment, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this.refreshPage$.next()), // Após a execução, emite um evento para os assinantes.
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um GET para pegar os dados de um atendimento especifico
   * @param id id do atendimento
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  findAppointment(id: number): Observable<any> {
    return this.http.get(`${this.baseURL}appointments/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um GET para obter todos os atendimentos cadastrados
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  listAppointments(): Observable<any> {
    let statuses = ['Aprovado', 'Cancelado', 'Encerrado'];
    return this.http.get(`${this.baseURL}appointments`, { headers: this.authService.getHeaders(), params: { status_list: statuses } })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um GET para obter todos os atendimentos cadastrados que estão pendentes
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  listPendingAppointments(): Observable<any> {
    let statuses = ['Pendente'];
    return this.http.get(`${this.baseURL}appointments`, { headers: this.authService.getHeaders(), params: { status_list: statuses } })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Busca o status com o nome Aprovado
   * @returns Um Observable contendo uma lista de campanhas ou erro.
   */
  getApprovedStatus(): Observable<any> {
    return this.http.get(`${this.baseURL}/status?name=Aprovado`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Busca o status com o nome Cancelado
   * @returns Um Observable contendo uma lista de campanhas ou erro.
   */
  getCanceledStatus(): Observable<any> {
    return this.http.get(`${this.baseURL}/status?name=Cancelado`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
 * @description Busca o status com o nome Encerrado
 * @returns Um Observable contendo uma lista de campanhas ou erro.
 */
  getClosedStatus(): Observable<any> {
    return this.http.get(`${this.baseURL}/status?name=Encerrado`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

}
