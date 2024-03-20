import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, throwError } from 'rxjs';
import { APP_CONFIG, Benefited, UserToken } from 'src/app/shared';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private baseURL!: string;
  private headers!: HttpHeaders;
  private user!: UserToken;

  constructor(private http: HttpClient) {
    this.baseURL = APP_CONFIG.baseURL;
    this.headers = new HttpHeaders({ 'Content-Type': 'application/json' });
  }

  /**
   * @description Faz um POST para inserir os dados de beneficiada
   * @param benefited O objeto beneficiada para ser enviado no body da requisição
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  saveBenefited(benefited: Benefited): Observable<any> {
    return this.http.post(`${this.baseURL}beneficiaries`, benefited, { headers: this.headers })
  }

  /**
   * @description Faz um GET para validar o código e prosseguir com o cadastro de beneficiada
   * @param code O código de acesso como parametro na URL
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  sendCode(code: string): Observable<any> {
    return this.http.get(`${this.baseURL}access_codes?code=${code}&used=false`, { headers: this.headers });
  }

  /**
   * @description Faz um GET para obter todos os Estados Civis cadastrados no sistema
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  getMaritalStatuses(): Observable<any> {
    return this.http.get(`${this.baseURL}marital_statuses`, { headers: this.headers });
  }

  /**
   * @description Faz um GET para obter todos os Programas Sociais cadastrados no sistema
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  getSocialPrograms(): Observable<any> {
    return this.http.get(`${this.baseURL}social_programs`, { headers: this.headers });
  }

  /**
   * @description Faz um GET para obter todos os Países cadastrados no sistema
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  getCountries(): Observable<any> {
    return this.http.get(`${this.baseURL}countries`, { headers: this.headers });
  }

  /**
   * @description Faz um GET para obter todos os Estados/Províncias cadastrados no sistema
   * @param countryId o Id do Pais selecionado para filtrar os estados
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  getStates(countryId: number): Observable<any> {
    return this.http.get(`${this.baseURL}states?country_id=${countryId}`, { headers: this.headers });
  }

  /**
   * @description Faz um GET para obter todas as cidades cadastradas no sistema
   * @param countryId o Id do Estado/Província selecionado para filtrar as cidades
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  getCities(stateId: number): Observable<any> {
    return this.http.get(`${this.baseURL}cities?state_id=${stateId}`, { headers: this.headers });
  }

  /**
   * @description Fazer
   * @param username
   * @param password 
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  login(value: { username: string, password: string }): Observable<any> {
    return this.http.post(`${this.baseURL}auth/login`, value, { headers: this.headers })
    .pipe(
      catchError(error => {
        return throwError(() => new Error(error.status));
      })
    );
  }

  setUser(user: UserToken) {
    this.user = user;
  }

  getUser(): UserToken {
    return this.user;
  }

}
