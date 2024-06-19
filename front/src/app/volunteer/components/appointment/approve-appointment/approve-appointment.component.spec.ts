import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ApproveAppointmentComponent } from './approve-appointment.component';

describe('ApproveAppointmentComponent', () => {
  let component: ApproveAppointmentComponent;
  let fixture: ComponentFixture<ApproveAppointmentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ApproveAppointmentComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ApproveAppointmentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
