import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject, catchError, tap, throwError } from 'rxjs';
import { AuthService } from 'src/app/auth';
import { CampaignPOST } from 'src/app/shared/models/campaign/campaign.model';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CampaignService {

  private baseURL: string;
  _refreshPage$ = new Subject<void>();

  constructor(private http: HttpClient, private authService: AuthService) {
    this.baseURL = environment.baseURL;
  }

  get refreshPage$() {
    return this._refreshPage$;
  }

  createCampaign(campaign: CampaignPOST): Observable<any> {
    return this.http.post(`${this.baseURL}campaigns`, campaign, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  deleteCampaign(id: number): Observable<any> {
    return this.http.delete(`${this.baseURL}campaigns/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  editCampaign(id: number, campaign: CampaignPOST): Observable<any> {
    return this.http.patch(`${this.baseURL}campaigns/${id}`, campaign, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  findCampaign(id: number): Observable<any> {
    return this.http.get(`${this.baseURL}campaigns/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }

  listCampaigns(): Observable<any> {
    return this.http.get(`${this.baseURL}campaigns`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }
}

