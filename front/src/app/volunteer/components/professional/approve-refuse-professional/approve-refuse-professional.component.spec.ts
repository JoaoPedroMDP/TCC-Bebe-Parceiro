import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ApproveRefuseProfessionalComponent } from './approve-refuse-professional.component';

describe('AproveRefuseProfessionalComponent', () => {
  let component: ApproveRefuseProfessionalComponent;
  let fixture: ComponentFixture<ApproveRefuseProfessionalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ApproveRefuseProfessionalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ApproveRefuseProfessionalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
