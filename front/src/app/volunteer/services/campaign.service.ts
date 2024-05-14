import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject, catchError, tap, throwError } from 'rxjs';
import { AuthService } from 'src/app/auth';
import { CampaignPOST } from 'src/app/shared/models/campaign/campaign.model';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CampaignService {

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
   * @description Envia uma requisição POST para criar uma nova campanha.
   * @param campaign Objeto com os dados da campanha para criação.
   * @returns Um Observable contendo os dados de resposta ou erro.
   */  
  createCampaign(campaign: CampaignPOST): Observable<any> {
    return this.http.post(`${this.baseURL}campaigns`, campaign, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Envia uma requisição DELETE para remover uma campanha pelo ID.
   * @param id Identificador da campanha a ser deletada.
   * @returns Um Observable contendo os dados de resposta ou erro.
   */ 
  deleteCampaign(id: number): Observable<any> {
    return this.http.delete(`${this.baseURL}campaigns/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Envia uma requisição PATCH para editar uma campanha existente.
   * @param id Identificador da campanha.
   * @param campaign Dados atualizados da campanha.
   * @returns Um Observable contendo os dados de resposta ou erro.
   */
  editCampaign(id: number, campaign: CampaignPOST): Observable<any> {
    return this.http.patch(`${this.baseURL}campaigns/${id}`, campaign, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Busca uma campanha específica pelo ID.
   * @param id Identificador da campanha.
   * @returns Um Observable contendo os dados da campanha ou erro.
   */
  findCampaign(id: number): Observable<any> {
    return this.http.get(`${this.baseURL}campaigns/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Busca todas as campanhas cadastradas.
   * @returns Um Observable contendo uma lista de campanhas ou erro.
   */
  listCampaigns(): Observable<any> {
    return this.http.get(`${this.baseURL}campaigns`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }
}

