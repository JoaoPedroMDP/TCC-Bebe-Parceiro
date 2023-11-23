import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { APP_CONFIG } from 'src/app/shared';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private baseURL = APP_CONFIG.baseURL;
  private headers = new HttpHeaders({ 'Content-Type': 'application/json'});
  constructor(private http: HttpClient) { }

  /**
   * @description Faz um GET para validar o código e prosseguir com o cadastro de 
   * @param codigo O código de acesso como parametro na URL
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  sendCode(codigo: string): Observable<any> {
    return this.http.get(`${this.baseURL}access_codes?code=${codigo}`, { headers: this.headers });
  }

  /**
   * @description Faz um GET para obter todos os Estados Civis cadastrados no sistema
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  getMaritalStatuses(): Observable<any>{
    return this.http.get(`${this.baseURL}marital_statuses`, { headers: this.headers });
  }

  getProgramasSociais(): Observable<any>{
    return this.http.get(`${this.baseURL}social_programs`, { headers: this.headers });
  }

  getCountries(): Observable<any>{
    return this.http.get(`${this.baseURL}countries`, { headers: this.headers });
  }

  getStates(countryId: number): Observable<any>{
    return this.http.get(`${this.baseURL}states?country_id=${countryId}`, { headers: this.headers }); 
  }

  getCities(stateId: number): Observable<any>{
    return this.http.get(`${this.baseURL}cities?state_id=${stateId}`, { headers: this.headers });    
  }
}
