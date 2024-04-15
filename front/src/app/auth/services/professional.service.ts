import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, throwError } from 'rxjs';
import { APP_CONFIG } from 'src/app/shared';
import { Professional } from 'src/app/shared/models/professional';

@Injectable({
  providedIn: 'root'
})
export class ProfessionalService {

  private baseURL!: string;

  constructor(private http: HttpClient) {
    this.baseURL = APP_CONFIG.baseURL;
  }

  /**
   * @description Faz um GET para obter todas as especialidades cadastradas no sistema
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  getSpecialities(): Observable<any> {
    return this.http.get(`${this.baseURL}specialities`);
  }

  /**
   * @description Faz um POST para salvar um profissional
   * @param professional O objeto contendo os dados do profissional
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  saveProfessional(professional: Professional): Observable<any> {
    return this.http.post(`${this.baseURL}professionals`, professional)
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }
}

