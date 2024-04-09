import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { Observable, catchError, tap, throwError } from 'rxjs';
import { APP_CONFIG, Benefited, UserToken } from 'src/app/shared';
import { Professional } from 'src/app/shared/models/professional';

@Injectable({
  providedIn: 'root'
})
export class ProfessionalService {
 

  private baseURL!: string;
  private headers!: HttpHeaders;

  constructor(private http: HttpClient, private cookieService: CookieService) {
    this.baseURL = APP_CONFIG.baseURL;
  }

  /**
   * @description Faz um GET para obter todas as cidades cadastradas no sistema
   * @param stateId o Id do Estado/Província selecionado para filtrar as cidades
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  
  /**
   * @description Obtém um usuário através de um cookie salvo no navegador
   * @returns Objeto do tipo `UserToken` contendo o token, dados e expiração
   */
  getUser(): UserToken {
    const userToken = this.cookieService.get('user');
    return userToken ? JSON.parse(userToken) : null;
  }

  /**
   * @description Armazena um cookie do usuário no navegador
   * @param user Objeto do tipo `UserToken` contendo o token, dados e expiração
   */
  setUser(user: UserToken) {
    this.cookieService.set('user', JSON.stringify(user), 1, '/');
  }

  
  getSpecialities(): Observable<any> {
    return this.http.get(`${this.baseURL}specialities`);
  }


  saveProfessional(professional: Professional): Observable<any> {
    return this.http.post(`${this.baseURL}professionals`, professional)
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }
}

