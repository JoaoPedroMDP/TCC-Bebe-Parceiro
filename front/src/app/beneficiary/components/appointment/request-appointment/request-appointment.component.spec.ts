import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RequestAppointmentComponent } from './request-appointment.component';

describe('RequestAppointmentComponent', () => {
  let component: RequestAppointmentComponent;
  let fixture: ComponentFixture<RequestAppointmentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RequestAppointmentComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RequestAppointmentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
