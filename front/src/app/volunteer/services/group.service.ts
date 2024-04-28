import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject, catchError, tap, throwError } from 'rxjs';
import { AuthService } from 'src/app/auth';
import { Group } from 'src/app/shared/models/volunteer/group.model';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class GroupService {

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
   * @param group O objeto especialidade para ser enviado no body da requisição
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  
  /**
   * @description Faz um GET para pegar os dados de uma especialidade especifica
   * @param id id da especialidade
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  findGroup(id: number): Observable<any> {
    return this.http.get(`${this.baseURL}groups/${id}`, { headers: this.authService.getHeaders() })
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
  listGroups(): Observable<any> {
    return this.http.get(`${this.baseURL}groups`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }
}
