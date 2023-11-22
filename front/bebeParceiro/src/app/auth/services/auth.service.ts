import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { APP_CONFIG, City, Country, State } from 'src/app/shared';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  baseURL = APP_CONFIG.baseURL;
  headers = new HttpHeaders({ 'Content-Type': 'application/json'});
  constructor(private http: HttpClient) { }

  /**
   * @description Faz um GET para validar o código e prosseguir com o cadastro de 
   * @param codigo O código de acesso
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  sendCode(codigo: string): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json'});
    return this.http.get(this.baseURL + 'access_codes?code=' + codigo, {headers});
  }

  getEstadoCivil(): Observable<any>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json'});
    return this.http.get(this.baseURL + 'marital_statuses', {headers});
  }

  getProgramasSociais(): Observable<any>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json'});
    return this.http.get(this.baseURL + 'social_programs', {headers});
  }

  getCountries(): Observable<any>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json'});
    return this.http.get(`${this.baseURL}countries`, {headers});
  }

  getStates(countryId: number): Observable<any>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json'});
    return this.http.get(`${this.baseURL}states?country_id=${countryId}`, {headers}); 
  }

  getCities(stateId: number): Observable<any>{
    const headers = new HttpHeaders({ 'Content-Type': 'application/json'});
    return this.http.get(`${this.baseURL}cities?state_id=${stateId}`, {headers});    
  }
}
