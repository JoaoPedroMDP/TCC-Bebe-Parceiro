import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { APP_CONFIG } from 'src/app/shared';

@Injectable({
  providedIn: 'root'
})
export class ProfessionalService {

  private baseURL!: string;

  constructor(private http: HttpClient) {
    this.baseURL = APP_CONFIG.baseURL;
  }

  getSpeciality(){}

  saveProfessional(){}
}
