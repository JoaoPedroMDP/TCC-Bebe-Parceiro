import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  baseURL = 'http://127.0.0.1:8000/access_codes';
  constructor(private http: HttpClient) { }

  validarCodigo(codigo: string): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json'});
    return this.http.get(this.baseURL + '?code=' + codigo, {headers});
  }
}
