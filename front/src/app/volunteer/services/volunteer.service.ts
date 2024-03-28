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
  createAcessCodes(amount: number): Observable<any> {
    return this.http.post(`${this.baseURL}access_codes`, amount, { headers: this.authService.getHeaders() })
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
  listAcessCodes(): Observable<any> {
    return this.http.get(`${this.baseURL}access_codes?used=false`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }
}
