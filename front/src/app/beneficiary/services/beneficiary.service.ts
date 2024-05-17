import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject, catchError, tap, throwError } from 'rxjs';
import { AuthService } from 'src/app/auth';
import { Swap } from 'src/app/shared';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class BeneficiaryService {

  private baseURL!: string;

  constructor(private http: HttpClient, private authService: AuthService) {
    this.baseURL = environment.baseURL;
  }

  /**
   * @description Faz um POST para criar uma troca
   * @param swap O objeto contendo os dados da troca
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  createSwap(swap: Swap): Observable<any> {
    return this.http.post(`${this.baseURL}swaps`, swap, { headers: this.authService.getHeaders() })
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
  deleteBeneficiary(id: number): Observable<any> {
    return this.http.delete(`${this.baseURL}beneficiaries/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um GET para pegar os dados de uma beneficiada especifica
   * @param id id da beneficiada
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  findBeneficiary(id: number): Observable<any> {
    return this.http.get(`${this.baseURL}beneficiaries/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  /**
   * @description Faz um GET para pegar os dados de uma campanha especifica
   * @param id id da campanha
   * @returns Um Observable contendo os dados de sucesso ou falha
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
   * @description Faz um GET para pegar os dados das campanhas abertas
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  listCampaigns(): Observable<any> {
    return this.http.get(`${this.baseURL}campaigns/open`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
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
   * @description Faz um GET para verificar se a beneciada pode fazer troca ou não
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  isBeneficiaryAbleToSwap(): Observable<any> {
    return this.http.get(`${this.baseURL}beneficiaries/can_request_swap`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }
}
