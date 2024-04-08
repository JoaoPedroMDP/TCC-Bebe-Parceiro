import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, throwError } from 'rxjs';
import { AuthService } from 'src/app/auth';
import { APP_CONFIG } from 'src/app/shared';

@Injectable({
  providedIn: 'root'
})
export class VolunteerService {

  private baseURL!: string;

  constructor(private http: HttpClient, private authService: AuthService) {
    this.baseURL = APP_CONFIG.baseURL;
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

  /**
   * @description Faz um DELETE para obter excluir uma beneficiada
   * @param id o Id da beneficiada a ser excluída
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  deleteBenefited(id: number): Observable<any> {
    return this.http.delete(`${this.baseURL}beneficiaries/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }
}
